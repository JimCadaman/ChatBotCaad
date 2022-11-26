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
    "Ola,", 
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
    "Não, muito obrigado",
    "A unifatec agradece",
    
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)


# In[ ]:


while True:
    mensagem = input("Manda uma mensagem para o bot do Caad:")
    if mensagem == "Não, muito obrigado":
        break
    resposta = chatbot.get_response(mensagem)    
    print(resposta)


# In[ ]:


chatbot.storage.drop()


# In[ ]:




