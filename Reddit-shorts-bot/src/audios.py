from gtts import gTTS


def salvandoConteudoEmAudio():
    with open("../reddit_posts/post_conteudo_reddit.txt", "r") as arquivo:
        conteudo = arquivo.read()

    tts_conteudo = gTTS(text=conteudo, lang='pt-br')
    conteudo_name = "../temp/audio_conteudo.mp3"
    tts_conteudo.save(conteudo_name)


def salvandoTituloEmAudio():
    with open("../reddit_posts/post_titulo_reddit.txt", "r") as arquivo:
        titulo = arquivo.read()
    
    tts_titulo = gTTS(text=titulo, lang='pt-br')
    titulo_name = "../temp/audio_titulo.mp3"
    tts_titulo.save(titulo_name)

print("Lendo arquivo de conteudo e salvando em audio")
salvandoConteudoEmAudio()
print("Lendo arquivo de titulo e salvando em audio")
salvandoTituloEmAudio()
print("Arquivos Lidos e salvos com sucesso")
