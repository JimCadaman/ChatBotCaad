#!/usr/bin/env python
# coding: utf-8

# In[1]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


# In[2]:


chatbot = ChatBot("CaadBot", tagger_language=ENGSM)
conversa = [
    "Ola", 
    "Como podemos te ajudar?",
    "Esqueci minha senha do Teams",
    "Poderia me informar seu nome completo?",
    "João da Silva Sauro",
    "Só um momento",    
    "Okay",
    "Resetamos sua senha para 1234",    
    "Okay, irei verificar",
    "Podemos ajudar em mais alguma coisa?",   
    "Sim, preciso saber acessar meu sistema academico",
    "Seu acesso ao sistema academico, ultiliza o e-mail institucional e a senha sua data de nascimento sem o /",
    "O e-mail institucional, é o mesmo do Teams?",
    "Sim",
    "Irei testar",
    "Podemos te ajudar em algo mais ?",
    "Gostaria de reclamar de um professor",
    "Este contato é somente para suporte técnico",
    "Com quem eu posso falar?",
    "Entre em contato com: Secretaria(41 91929395) para realções de inscrições e retirada de informações sobre cursos, Financeiro(41 91959697) para cobrança em geral, Direção Academica(41 2738475) para reclamações em relação a professores e funcionarios,", 
    "Beleza",
    "Mais alguma coisa que podemos te ajudar ?",
    "Não, muito obrigado",
    "A unifatec agradece",
    "Obrigado e tenha um bom dia",
    
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)


# In[3]:


while True:
    mensagem = input("Manda uma mensagem para o bot do Caad:")
    if mensagem == "Obrigado e tenha um bom dia":
        break
    resposta = chatbot.get_response(mensagem)    
    print(resposta)


# In[4]:


chatbot.storage.drop()


# In[ ]:




