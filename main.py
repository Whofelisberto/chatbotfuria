import streamlit as st
import os
from dotenv import load_dotenv
import openai

# função que guarda o token da api no arquivo env e chama sem mostrar a chave

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# título da página
st.set_page_config(
page_title="FURIA CHATBOT",
layout="wide")

# barra de navegação
st.sidebar.image("https://images.seeklogo.com/logo-png/42/2/furia-esports-logo-png_seeklogo-428783.png")
st.sidebar.title("")
pagina = st.sidebar.selectbox("", ["CHATBOT"])

st.subheader("Bem-vindo ao chatbot da FURIA!")
st.write("Fique por dentro das notícias do time, os jogadores, eventos e etc...")

# função para criar a página
def chat():

# armazenamento de informações da furia para o chatbot

    informacoes_furia = """Você é um chatbot do time de CS da FURIA.

    O que você deve saber sobre a FURIA:
    qual é o nome do molodoy? Danil Golubenko
    qual é a função do molodoy na equipe da furia? o jogador é o mais novo AWPer
    quem é Hepa?  Seu nome é juan borges treinador assistente da furia de cs2.
    quais jogadores entraram no lugar do chelo e skullz? molodoy e yekindar 
    Quantos anos tem o Yekindar? 25 anos
    de qual time era o Yekindar? era do time da Liquid
    de qual time de cs2 era o molodoy? era do time da AKML. jovem talento que vem se destacando no cenário do cs2.
    qual é o rating do molodoy? 1.21
    quantos anos tem o novo jogador da furia? molodoy tem apenas 20 anos
    qual é o próximo jogo da furia? FURIA x The MongolZ pela PGL Astana 2025
    ultimos resultados da furia? a furia perdeu de 2x0 para para The MongolZ,  Virtus.Pro , 2x1 para a complexity
    qual foi o ultimo jogo que a furia ganhou? A furia ganhou da Betclic por 2x0
    história do fallen : Gabriel 'FalleN' Toledo começou seu caminho no Counter-Strike 1.6 aos 12 anos, quando se juntou ao time da Soldiers of Fire. Em 2005, o awper teve seu primeiro destaque nacional jogando pela Crashers, ao disputar as qualificatórias da World Cyber Games (WCG) de 2005 a 2008. Mas foi pela FireGamers que a chance veio em 2009.
    quando organização da furia foi fundada: A organização de esports FURIA foi fundada em 8 de agosto de 2017, na cidade de Uberlândia, Minas Gerais. O projeto nasceu da colaboração entre o empresário Jaime Pádua, o jogador de pôquer profissional André Akkari, e os empresários Cris Guedes e Nicholas Nogueira. Inicialmente, a FURIA focou no cenário competitivo de Counter-Strike: Global Offensive (CS:GO), mas rapidamente expandiu sua atuação para outras modalidades, como League of Legends, VALORANT, Rainbow Six Siege, Rocket League, Apex Legends, Futebol de 7 e PUBG Mobile. Desde sua fundação, a FURIA tem se destacado no cenário de esports, conquistando títulos importantes e estabelecendo parcerias estratégicas com marcas como Lenovo, Red Bull, PokerStars, Hellmann’s e Cruzeiro do Sul Virtual. Além disso, a organização tem investido em projetos socioculturais, como o "Futuro em Jogo", que visa promover a inclusão de jovens negros e pardos no mercado de trabalho .
    Atualmente, a FURIA é reconhecida como uma das principais organizações de esports do Brasil e da América Latina, com presença internacional em alguns países.
    Ranking HLTV do time que é o: °18
    Novo lançamento de drop da furia X longitech 
    Nomes dos jogadores: FalleN, Yuurih, Kscerato, Molodoy, Yekindar
    Próximos eventos que vão jogar: PGL Astana 2025, IEM Dallas 2025, BLAST.tv Austin Major 2025
    Jogadores que saíram da equipe recentemente: Chello e Skull
    O coach da equipe é o: Sidde
    títulos ganhados: a furia ganhou 4 títulos de acordo com a hltv.org
    O site deles é: https://www.furia.gg/
    qual é o instagram dos jogadores da furia? @danil.molodoy_, @fallen , @kscerato , @yek1ndar , @yuurihfps
    qual é o canal de vlog da furia? https://www.youtube.com/@FURIAggCS
    quem foi o melhor jogador da furia de cs2 em 2024? 
    quais jogadores da furia entraram nos melhores jogadores do mundo de acordo com o site da hltv.org?
    O que vende no site: camisetas, bonés, mochilas, calças, jaquetas, croppeds, shorts, moletons, meias e buckets
    tem Promoções de acessórios no site? Sim"""

    if "messages" not in st.session_state:
        st.session_state.messages = []

# mostrar mensagens anteriores

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

# input do user

    if prompt := st.chat_input("Pergunte algo sobre a FURIA..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

# resposta do chatbot do openai

        with st.spinner("Respondendo..."):
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": informacoes_furia},
                    *st.session_state.messages
                ]
            )
            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.chat_message("assistant").write(reply)


# chamando a função chat

if pagina == "CHATBOT":
    chat()
