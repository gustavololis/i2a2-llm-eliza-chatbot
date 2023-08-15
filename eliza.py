import re
import random

patterns_responses =    {
    r'.*ideação suicida.*|.*pensamentos suicidas.*|.*suicídio.*|.*quero morrer.*|.*vontade de morrer.*|.*me matar.*': [
        "Sinto muito que você esteja passando por isso, mas é importante que você procure ajuda profissional imediatamente.",
        "Esses pensamentos são sérios e não devem ser ignorados. Recomendo entrar em contato com um profissional de saúde mental.",
        "Neste momento, é fundamental buscar apoio de amigos, familiares ou profissionais de saúde. Não hesite em procurar ajuda!",
        "Se você estiver passando por uma crise, por favor, ligue para um serviço de apoio ou vá ao pronto-socorro mais próximo.",
        "Entendo que você pode estar se sentindo sobrecarregado, mas é essencial falar com alguém sobre isso. Procure ajuda."
    ],
     r'.*automutilação.*|.*machucar-me.*|.*ferir-me.*|.*cortar-me.*|.*me cortar.*|.*me machucar.*': [
        "Sinto muito que você esteja se sentindo assim, mas a automutilação não é uma solução saudável para lidar com a dor emocional.",
        "Estou aqui para ajudar e ouvir. Se você está pensando em se automutilar, recomendo que procure ajuda profissional imediatamente.",
        "Automutilação não é uma forma eficaz de lidar com o que você está sentindo. Por favor, busque apoio de um profissional de saúde mental.",
        "Lembre-se de que existem outras maneiras de enfrentar seus sentimentos. Entrar em contato com um terapeuta pode ser um passo importante para encontrar alternativas saudáveis.",
        "Se você estiver em perigo imediato ou precisar de apoio imediato, não hesite em ligar para um serviço de apoio ou procurar ajuda médica."
    ],
    r'.*me sinto (.*)': [
        "Por que você se sente {0}?",
        "Você poderia me contar mais sobre por que se sente {0}?",
        "Eu entendo como você se sente {0}.",
        "É normal se sentir {0}.",
        "Como você lida com se sentir {0}?",
        "O que você faz quando está se sentindo {0}?",
        "Você já conversou com alguém sobre se sentir {0}?"
    ],
    r'.*estou (.*)': [
        "Por que você está {0}?",
        "Você está {0}? Como tem lidado com isso?",
        "Como tem sido para você estar {0}?",
        "O que você acha que pode estar deixando você {0}?",
        "Você gostaria de mudar essa situação?",
        "Já aconteceu antes de você estar {0}?"
    ],
    r'.*você é (.*)': [
        "Por que você acha que sou {0}?",
        "Você está me descrevendo como {0}?",
        "Você acredita que sou {0}? Por quê?",
        "Às vezes as pessoas veem as coisas de maneiras diferentes. Como você chegou a essa conclusão?",
        "Meu objetivo é te ajudar, independentemente de ser {0} ou não.",
        "O que você acha que eu deveria ser?"
    ],
    r'.*você (.*)': [
        "Vamos focar em você. Por que você está falando sobre mim?",
        "Por que você está interessado em saber sobre mim?",
        "Vamos voltar ao assunto sobre você.",
        "Acredito que você está aqui para conversar sobre você mesmo. O que você gostaria de falar?"
    ],
    r'.*não (.*)': [
        "Por que você não {0}?",
        "Você gostaria de {0}? Por que não?",
        "Entendo que você não {0}. Alguma razão específica?",
        "O que você acha que aconteceria se você {0}?",
        "Há alguma razão especial que o impede de {0}?"
    ],
    r'.*nome é (.*)': [
        "Olá, {0}! Como posso ajudá-lo hoje?",
        "Bem-vindo, {0}! Estou aqui para ouvi-lo.",
        "É um prazer conhecê-lo, {0}. Como posso ser útil?",
        "Seu nome, {0}, é muito bonito. Como posso auxiliá-lo?"
    ]
}

sentiments =     {
    "negative": ["triste", "frustrado", "raiva", "chateado", "infeliz", "preocupado", "nervoso", "ansioso", "inseguro", "solitário", "desesperado", "tristeza", "desanimado", "sem esperança", "sem ânimo", "medo"],
    "positive": ["feliz", "animado", "alegre", "satisfeito", "otimista", "grato", "confiante", "realizado", "calmo", "amor", "paz", "esperança", "alegria", "contente", "forte", "motivado"],
    "neutral": ["pensativo", "reflexivo", "neutro", "indiferente", "ambivalente", "ponderando", "questionando", "analítico", "observador"]
}

# Função otimizada para analisar sentimentos
def analyze_sentiment(input_text):
    input_text_lower = input_text.lower()
    sentiment_scores = {sentiment: sum(1 for word in words if word in input_text_lower) for sentiment, words in sentiments.items()}
    max_sentiment = max(sentiment_scores, key=sentiment_scores.get)
    return max_sentiment

# Função para gerar respostas
def eliza_response(input_text):
    for pattern, responses in patterns_responses.items():
        match = re.match(pattern, input_text.lower())
        if match:
            if pattern in patterns_responses:
                response = random.choice(patterns_responses[pattern])
                return response.format(*match.groups())
            else:
                return "Conte-me mais."
    sentiment = analyze_sentiment(input_text)
    if sentiment == "negative":
        return "Eu sinto muito que você esteja se sentindo assim. Posso te ajudar de alguma forma?"
    elif sentiment == "positive":
        return "Fico feliz em saber que você está se sentindo bem! Como posso contribuir para esse sentimento?"
    else:
        return "Conte-me mais."
'''
# Função para lidar com o botão "Enviar"
def on_send_button_clicked(b):
    user_input = input_box.value
    if user_input.lower() in ['sair', 'adeus', 'tchau', 'fim']:
        with output:
            clear_output()
            print("Eliza: Até logo! Espero que tenha se sentido melhor.")
    else:
        response = eliza_response(user_input)
        with output:
            clear_output()
            print(f"Você: {user_input}")
            print(f"Eliza: {response}\n")
    input_box.value = ""

# Configuração dos widgets e início do chat
input_box = widgets.Text(placeholder="Digite sua mensagem aqui...", description="Você:")
send_button = widgets.Button(description="Enviar")
output = widgets.Output()

send_button.on_click(on_send_button_clicked)

chat_layout = widgets.VBox([output, input_box, send_button])
display(chat_layout)

with output:
    clear_output()
    print("Eliza: Olá! Sou Eliza, o terapeuta virtual. Como posso ajudá-lo hoje?")
'''