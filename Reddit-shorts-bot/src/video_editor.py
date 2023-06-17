from moviepy.editor import VideoFileClip
import random

def lerArquivosAudioVideo(caminhoTitulo, caminhoConteudo, caminhoVideo):

    video = VideoFileClip(caminhoVideo)
    tamanhoVideo = video.reader.size()
    video.close()

    audio_titulo = VideoFileClip(caminhoTitulo)
    tamanhoTitulo = audio_titulo.reader.size()
    audio_titulo.close()

    audio_conteudo = VideoFileClip(caminhoConteudo)
    tamanhoConteudo = tamanhoConteudo.reader.size() 
    audio_conteudo.close()

    return video, audio_titulo, audio_conteudo, tamanhoConteudo, tamanhoTitulo, tamanhoVideo

caminhoTitulo = "../temp/audio_titulo.mp3"
caminhoConteudo = "../temp/audio_conteudo.mp3"
caminhoVideo = "../background_videos/video_mine.mp4"

video, audio_titulo, audio_conteudo, tamanhoConteudo, tamanhoTitulo, tamanhoVideo = lerArquivosAudioVideo(caminhoTitulo,caminhoConteudo,caminhoVideo)

tamanhoClipe = tamanhoConteudo + tamanhoTitulo

comecoClipe = random(5,(tamanhoVideo-tamanhoClipe-5))
fimClipe = comecoClipe + tamanhoClipe
