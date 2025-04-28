import streamlit as st
import openai

# título da página
st.set_page_config(
page_title="FURIA CHATBOT",
layout="wide")

# barra de navegação
st.sidebar.image("https://images.seeklogo.com/logo-png/42/2/furia-esports-logo-png_seeklogo-428783.png")
st.sidebar.title("")
pagina = st.sidebar.radio("",("HOME", "CHAT", "LOJA", "CONTATO" ))

# funções para cada página
def home():
    st.title("HOME")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p>Uma organização de esports que nasceu do desejo de representar o Brasil no CS e conquistou muito mais que isso: expandimos nossas ligas, disputamos os principais títulos, adotamos novos objetivos e ganhamos um propósito maior. Somos muito mais que o sucesso competitivo. Somos um movimento sociocultural. Nossa história é de pioneirismo, grandes conquistas e tradição. Nosso presente é de desejo, garra e estratégia. A pantera estampada no peito estampa também nosso futuro de glória. Nossos pilares de performance, lifestyle, conteúdo, business, tecnologia e social são os principais constituintes do movimento FURIA, que representa uma unidade que respeita as individualidades e impacta positivamente os contextos em que se insere. Unimos pessoas e alimentamos sonhos dentro e fora dos jogos.</p>", unsafe_allow_html=True)
    left, middle, right = st.columns(3)
    left.image("https://furiagg.fbitsstatic.net/media/banner-galeria-desk-mha.jpg?v=202410241902")
    middle.image("https://furiagg.fbitsstatic.net/media/banner_mobile_-_champion_2.jpg?v=202409241435")
    right.image("https://furiagg.fbitsstatic.net/media/collection-fib.jpg?v=202409241435")
    st.image("https://furiagg.fbitsstatic.net/img/b/1be4afd5-a727-4555-81fd-e779a32578be.jpg?w=1920&v=no-change")

# imagens do site da furia , com o link para a loja

def loja():
    st.title("🛒 LOJA")
    st.markdown("[Mais lançamentos no site da FURIA](https://www.furia.gg/)")
    left, middle, right = st.columns(3)
    left.image("https://furiagg.fbitsstatic.net/img/p/camiseta-oficial-furia-adidas-preta-150265/337491-1.jpg?w=468&h=468&v=202503281009")
    middle.image("https://furiagg.fbitsstatic.net/img/p/camiseta-oversized-furia-x-zor-verde-estonada-150242/337333-2.jpg?w=468&h=468&v=no-value")
    right.image("https://furiagg.fbitsstatic.net/img/p/calca-jogger-furia-preta-150198/337022-1.jpg?w=468&h=468&v=no-value")
    left2, middle2, right2 = st.columns(3)
    left2.image("https://furiagg.fbitsstatic.net/img/p/jaqueta-college-my-hero-academia-x-furia-azul-150230/337255-2.jpg?w=468&h=468&v=no-value")
    middle2.image("https://furiagg.fbitsstatic.net/img/p/camiseta-oversized-furia-x-zor-woodhorse-marrom-150243/337340-2.jpg?w=468&h=468&v=no-value")
    right2.image("https://furiagg.fbitsstatic.net/img/p/jaqueta-my-hero-academia-x-furia-izuku-midorya-verde-150231/337262-1.jpg?w=468&h=468&v=no-value")

def chat():
    st.title("CHAT")
    st.markdown("Pergunte algo sobre a furia, organização , jogadores, loja, próximos jogos e...")

# API do chatgpt , para nosso chatbot. (eu poderia usar o .env para não enviar para o git a chave da api, mas como deve ser testada vou deixar assim mesmo depois de um tempo eu mudo.)

    chave_api = "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"
    openai.api_key = chave_api

# armazenamento de informações da furia para o chatgtp

    informacoes_furia = """Você é um chatbot do time de CS da FURIA.

    O que você deve saber sobre a FURIA:

    quando organização da furia foi fundada: A organização de esports FURIA foi fundada em 8 de agosto de 2017, na cidade de Uberlândia, Minas Gerais. O projeto nasceu da colaboração entre o empresário Jaime Pádua, o jogador de pôquer profissional André Akkari, e os empresários Cris Guedes e Nicholas Nogueira. Inicialmente, a FURIA focou no cenário competitivo de Counter-Strike: Global Offensive (CS:GO), mas rapidamente expandiu sua atuação para outras modalidades, como League of Legends, VALORANT, Rainbow Six Siege, Rocket League, Apex Legends, Futebol de 7 e PUBG Mobile. Desde sua fundação, a FURIA tem se destacado no cenário de esports, conquistando títulos importantes e estabelecendo parcerias estratégicas com marcas como Lenovo, Red Bull, PokerStars, Hellmann’s e Cruzeiro do Sul Virtual. Além disso, a organização tem investido em projetos socioculturais, como o "Futuro em Jogo", que visa promover a inclusão de jovens negros e pardos no mercado de trabalho .
    Atualmente, a FURIA é reconhecida como uma das principais organizações de esports do Brasil e da América Latina, com presença internacional em alguns países.

    Ranking HLTV do time que é o: °16

    Nomes dos jogadores: FalleN, Yuurih, Kscerato, Molodoy, Yekindar

    Próximos eventos que vão jogar: PGL Astana 2025, IEM Dallas 2025, BLAST.tv Austin Major 2025

    Jogadores que saíram da equipe recentemente: Chello e Skull

    O coach da equipe é o: Sidde

    títulos ganhados: a furia ganhou 4 títulos de acordo com a hltv.org

    O site deles é: https://www.furia.gg/

    O que vende no site: camisetas, bonés, mochilas, calças, jaquetas, croppeds, shorts, moletons, meias e buckets

    Promoções de acessórios no site

    Sorteios de itens"""

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

def contato():
    st.title("CONTATO")
    st.text_input("Seu nome")
    st.text_input("Seu email")
    st.text_area("Mensagem")
    st.button("Enviar")



# mostrar a página selecionada

if pagina == "HOME":
    home()
elif pagina == "LOJA":
    loja()
elif pagina == "CHAT":
    chat()
elif pagina == "CONTATO":
    contato()
