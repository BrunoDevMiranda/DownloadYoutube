from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import subprocess
import re

url = "https://youtu.be/KD0e0ihWHE0?si=BCgKbziC8S2oCOC8"
output_path = 'H:/tiktoke/edit/'
video_res = '1080p'

# Pasta temporária para salvar arquivos separados
temp_folder = os.path.join(output_path, "temp")
os.makedirs(temp_folder, exist_ok=True)


# Função para limpar o nome do arquivo
def sanitize_filename(filename):
    # Remove caracteres inválidos
    filename = re.sub(r'[\\/:*?"<>|]', '', filename)
    # Limita o comprimento do nome (opcional)
    filename = filename[:255]
    return filename


# Cria instância do YouTube
yt = YouTube(url, on_progress_callback=on_progress)

# --- SELECIONAR VÍDEO ---
print("\nBuscando stream de vídeo...")
video_stream = None

# Primeiro tentamos encontrar a resolução desejada (1080p)
for stream in yt.streams:
    if stream.resolution == video_res and stream.mime_type == "video/mp4":
        video_stream = stream
        print(f"✅ Vídeo {video_res} encontrado!")
        break

# Se não encontrar, escolher a maior resolução disponível
if not video_stream:
    video_streams = [s for s in yt.streams if s.resolution and s.mime_type == "video/mp4"]
    if not video_streams:
        print("❌ Nenhum stream de vídeo MP4 disponível.")
        exit()

    video_streams.sort(key=lambda x: int(x.resolution.replace("p", "")), reverse=True)
    video_stream = video_streams[0]
    print(f"⚠️ Vídeo {video_res} não encontrado. Usando a próxima melhor resolução: {video_stream.resolution}")

video_file = os.path.join(temp_folder, "video.mp4")
video_stream.download(output_path=temp_folder, filename="video.mp4")
print("✅ Vídeo baixado")

# --- BAIXAR ÁUDIO ---
print("\nBaixando melhor áudio disponível...")
audio_stream = yt.streams.filter(only_audio=True).first()
audio_file = os.path.join(temp_folder, "audio.mp3")
audio_stream.download(output_path=temp_folder, filename="audio.mp3")
print("✅ Áudio baixado")

# --- COMBINAR ÁUDIO E VÍDEO COM FFmpeg ---
print("\nCombinando áudio e vídeo...")

# Limpa o título do vídeo para criar um nome de arquivo seguro
cleaned_title = sanitize_filename(yt.title)
final_output = os.path.join(output_path, f"{cleaned_title}_com_audio.mp4")

ffmpeg_command = [
    "ffmpeg",
    "-i", video_file,
    "-i", audio_file,
    "-c:v", "copy",
    "-c:a", "aac",
    final_output
]

subprocess.run(ffmpeg_command, check=True)

# Limpar temporários (opcional)
os.remove(video_file)
os.remove(audio_file)
os.rmdir(temp_folder)

print(f"\n✅ Download concluído! Arquivo salvo em:\n{final_output}")