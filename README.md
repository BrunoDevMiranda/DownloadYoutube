# YouTube Video Downloader 🎥

> Um script simples e eficiente para baixar vídeos do YouTube com resolução escolhida e juntar com o áudio usando FFmpeg.

---

## 📌 Sobre

Este é um script em Python que permite baixar vídeos do YouTube com a melhor qualidade disponível (ex: 1080p) e combinar vídeo + áudio utilizando `FFmpeg`. Ele é ideal para quem quer automatizar downloads ou integrar a workflows mais amplos.

---

## ✅ Funcionalidades

- [x] Baixa vídeo na resolução desejada (ex: `1080p`)
- [x] Se não encontrar a resolução desejada, usa a maior disponível
- [x] Baixa o melhor áudio disponível
- [x] Combina vídeo e áudio com `FFmpeg`
- [x] Trata nomes de arquivos com caracteres especiais
- [x] Suporte a customização da pasta de saída

---

## 🧰 Requisitos

Antes de rodar, certifique-se de ter instalado:

- [Python 3.8+](https://www.python.org/downloads/) 
- [FFmpeg](https://ffmpeg.org/download.html)  (instalado e no PATH)
- Bibliotecas Python:
  - `pytubefix`

Instale as dependências com:

```bash
pip install pytubefix



▶️ Como Usar
Clone este repositório:
bash


1
2
git clone https://github.com/seu-usuario/youtube-downloader.git 
cd youtube-downloader
Instale as dependências:
bash


1
pip install pytubefix
Certifique-se de ter o ffmpeg instalado e acessível via terminal.
Execute o script:
bash


1
python download_video.py
O vídeo será salvo na pasta definida .
⚙️ Configurações Personalizáveis
Você pode editar estas variáveis no topo do código:

python


1
2
3
url = "https://youtu.be/exemplo"          # URL do vídeo
output_path = 'pasta para salva os videos # Pasta de destino
video_res = '1080p'                       # Resolução desejada
🤝 Contribuição
Contribuições são sempre bem-vindas!
Se quiser adicionar novas funcionalidades como:

Interface gráfica
Download de playlists
Converter para MP3
Escolher formato de saída
É só abrir uma PR 😊
