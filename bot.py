import os

import random
import re
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	guild = discord.utils.get(client.guilds, name=GUILD)
	print(
		f'{client.user.name} is connected to the following guild: \n'
		f'{guild.name}(id: {guild.id})'
		)
	activity = discord.Activity(name="Jojo Part 4: Diamond is Unbreakable", type=discord.ActivityType.watching)
	await client.change_presence(status=discord.Status.online, activity=activity)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    metalgear_quotes = [
        'To Do The Right Thing, You Sometimes Have To Leave The Things You Care About Behind.',
        'Para fazer a coisa certa, as vezes é necessário deixar coisas que importam para trás.',
        
            'You’ve got it all wrong. You were the lightning in that rain. You can still shine through the darkness',
            'Você é o raio dentro da tempestade, você consegue brilhar dentro da escuridão.',
            'There’s no such thing in the world as absolute reality. Most of what they call real is actually fiction. What you think you see is only as real as your brain tells you it is.',
            'Não existe nada no mundo que seja uma realidade absoluta, a maioria das coisas que chamamos de reais é ficção. O que você acredita que vê só é real porque sua mente diz que é.',
            'I think at any time, any place, people can fall in love with each other. But if you love someone, you have to be able to protect them.',
            'Eu acredito que em qualquer hora, qualquer lugar, as pessoas podem se apaixonar umas pelas outras. Mas se você ama alguém, você deve ser capaz de protegê-la',
            'We can tell other people about having faith. What we had faith in. What we found important enough to fight for. It’s not whether you were right or wrong, but how much faith you were willing to have, that decides the future',
            'Nós podemos falar sobre fé para outras pessoas. No que acreditamos. O que consideramos importante o bastante para lutar. Não é sobre estar certou ou errado, mas no quanto você esta disposta a acreditar, é isso que vai decidir o futuro.',
            'Don’t regret your past. Learn from it. Regrets only make a person weaker',
            'Não se arrependa so seu passado. Aprenda com ele. Arrependimentos só tornam as pessoas mais fracas.',
            'Earth may not be forever, but we still have the responsibility to leave what traces of life we can. Building the future and keeping the past alive are one and the same thing.',
            'A terra talvez não dure para sempre, mas ainda temos a responsabilidade de deixar o quanto pudermos dos traços de vida. Constuir um futuro e manter o passado vivo são a mesma coisa.',
            'Building the future and keeping the past alive are one and the same thing.',
            'Construir um futuro e manter o passado vivo são a mesma coisa.',
            'Life isn’t just about passing on your genes. We can leave behind much more than just DNA. Through speech, music, literature and movies..what we’ve seen, heard, felt..anger, joy and sorrow..these are the things I will pass on. That’s what I live for.',
            'A vida não é sobre passar nossos genes adiante. Nós podemos deixar muito mais do que o DNA. Através da escrita, música, literatura e filmes.... o que nós vemos, ouvimos, sentimos...irritamos, o que nos trás felicidade e tristeza... Essas são as coisas que irei passar adiante. Esse é o propósito pelo qual eu vivo.',
            'We need to pass the torch, and let our children read our messy and sad history by its light.We have all the magic of the digital age to do that with.',
            'Nós precisamos passar a tocha adiante, e deixar que nossos filhos leiam nossa triste e bagunçada história pela visão deles. Temos a magia da era digital para realizar isso',
            'What’s important is that you choose life..and then live',
            'O importante é você escolher a vida... e então viver',
            'We’re not tools of the government or anyone else..Fighting was the only thing I was good at, but at least I always fought for what I believed in.',
            'Nós não somos ferramentas do governo e de ninguém... Lutar era a única coisa que eu sabia fazer mas... pelo menos eu lutava por aquilo que eu acreditava...',
            'You can’t keep attacking yourself for things that happened in the past. That road leads to madness, believe me.',
            'Você não pode continuar se culpando pelas coisas que aconteceram no passado. Esse caminho o leva a loucura e perda total da sanidade, acredite...',
            'Pain gets the better of us all.',
            'A dor tira o que tem de melhor em nós.',
            'Real heroes are never as polished as the legends That surround them.',
            'Os verdadeiros heróis nunca são tão perfeitinhos como as lendas que os se ouvem deles.',
            'I won\'t scatter your sorrow to the heartless sea. I will always be with you.',
            'Eu não deixarei que seus sofrimentos se percam no mar... Eu estarei com vocês para sempre.',
            'You can’t wait to be loved. You have to go out and find it.',
            'Você não pode esperar por magicamente ser amado. Você tem que sair procurar por um.',
            'I realized that you can’t just wish for a happy family — you have to make it happen. I only wish I knew that sooner.',
            'Eu percebi que você não pode somente querer uma família feliz... você tem que fazer com que isso aconteça. Eu só queria ter descoberto isso antes...',
            'You can stop being part of a mistake, starting now.',
            'Você pode deixar de ser um erro, começando agora.',
            'We are all born with an expiration date. No one lasts forever. Life is but a grace period for turning the best of our genetic material into the next generation.',
            'Todos nascemos com uma data de validade. Ninguém vive para semre. A vida é um belo periódo que experienciamos para prosperar as futuras gerações.',
            'Pick your own name, and your own life. And find something worth passing on.',
            'Escolha o seu próprio nome, e sua própria vida. E procure em algo para acreditar e passar adiante.',
            'Death is tragic, but life is miserable.',
            'A morte é trágica, mas a vida é miserável',
            'The foibles of politics and the march of time can turn friends into enemies just as easily as the wind changes. Ridiculous, isn’t it?',
            'We have no tomorrow. But we can still have hope for the future.',
            'To a ruler, an everlasting enemy is convenient.',
            'Para um líder, um eterno inimigo é algo bem conveniente...',
            'A strong man doesn’t need to read the future. He makes his own.',
            'Uma pessoa forte não precisa ler o seu futuro. Ela o cria por si mesma!',
            'He who controls the battlefield, controls history.',
            'Aquele que controla o campo de batalha, controla a história',
            'Unfortunately, killing is one of those things that gets easier the more you do it.',
            'Infelizmente, matar é uma das coisas que se tornar fácil a cada vez que o faz.',
            'It’s easy to forget what a sin is in the middle of a battlefield.',
            'É fácil esquecer o que é um pecado no meio do campo de batalha',
            'I don’t have any more tears to shed.',
            'Eu não tenho mais lágrimas para compartilhar.',
            'No one quite knows who or what they are.',
            'Ninguem no mundo pode saber quem ou que ele mesmo é.',
            'A name means nothing on the battlefield.',
            'Um nome não significa nada no campo de batalha.',
            'O que terá que ser será. Não se preocupe com o que as outras pessoas podem achar, você estará bem, eu prometo.',
            'É somente uma dia ruim, não uma vida ruim.',
            'Acredite em você mesmo e crie o seu próprio destino, não tema o fracasso.',
            'Esta tudo bem se sentir perdido.',
            'O tempo que importa é agora.',
            'Nunca desista, tudo o que vale a pena é difícil.',
            'A vida é um risco digno',
            'Expect nothing and appreciate everything.',
            'Não espere por nada e aprecie cada momento.'





        ,
    ]

    if "boss" in message.content.lower():
        response = random.choice(metalgear_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

    if "lain" in message.content.lower():
        selected_message = random.choice(await message.channel.history(limit=250).flatten())
        await message.channel.send(re.sub('<@.*?>',"Vejamos...",selected_message.content, flags=re.DOTALL))
    elif message.content == 'raise-exception':
        raise discord.DiscordException
client.run(TOKEN)