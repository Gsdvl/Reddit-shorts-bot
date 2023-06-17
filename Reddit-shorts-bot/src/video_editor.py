from moviepy.editor import *
import random

def lerArquivosAudioVideo(caminhoTitulo, caminhoConteudo, caminhoVideo):

    video = VideoFileClip(caminhoVideo)
    tamanhoVideo = video.duration
    video.close()

    audio_titulo = AudioFileClip(caminhoTitulo)
    tamanhoTitulo = audio_titulo.duration
    audio_titulo.close()

    audio_conteudo = AudioFileClip(caminhoConteudo)
    tamanhoConteudo = audio_conteudo.duration
    audio_conteudo.close()

    return video, audio_titulo, audio_conteudo, tamanhoConteudo, tamanhoTitulo, tamanhoVideo

caminhoTitulo = "../temp/audio_titulo.mp3"
caminhoConteudo = "../temp/audio_conteudo.mp3"
caminhoVideo = "../backgroud_videos/video_mine.mp4"

video, audio_titulo, audio_conteudo, tamanhoConteudo, tamanhoTitulo, tamanhoVideo = lerArquivosAudioVideo(caminhoTitulo,caminhoConteudo,caminhoVideo)

tamanhoClipe = tamanhoConteudo + tamanhoTitulo

print(tamanhoVideo, tamanhoClipe)

comecoClipe = random.randrange(5,int(tamanhoVideo-tamanhoClipe-5))
fimClipe = comecoClipe + tamanhoClipe

video = VideoFileClip(caminhoVideo).subclip(comecoClipe, fimClipe)
video = video.resize(height=1920)
video = video.crop(x1=1166.6,y1=0,x2=2246.6,y2=1920)

video.audio = concatenate_audioclips([AudioFileClip(caminhoTitulo), AudioFileClip(caminhoConteudo)])

titulo = open("../reddit_posts/post_titulo_reddit.txt", "r", encoding="utf-8")
conteudo = open("../reddit_posts/post_conteudo_reddit.txt", "r", encoding="utf-8")

texto = TextClip(titulo.read() + '\n\n' + conteudo.read(),
                fontsize=75,
                color="white",
                method="caption",
                stroke_color="white",
                stroke_width=3,
                size=(900, 1780)
                ).set_pos('center').set_duration(tamanhoClipe) 

titulo.close()
conteudo.close()

CompositeVideoClip([video, texto]).write_videofile('../edited_videos/video_editado.mp4')