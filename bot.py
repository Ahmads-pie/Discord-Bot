import discord
import random
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
from discord.ext import commands
heart_symbol = u'\u2764'
bot = commands.Bot(command_prefix = 's.')
@bot.event
async def on_ready():
    print('S is ready')
    
@bot.command()
async def Help(ctx):
    await ctx.send("These are the commands that you can ask me to do: \n -Anime: To Give you an anime recommendation\n \n -clear [write the ammount of the message that you wanna delete]: to delete some of the chat messages\n \n -password: to give you a real hard password to guess\n -pepo:to send pepo")

@bot.command()
async def ping(ctx):
    await ctx.send(f'it takes {round (bot.latency * 1000)}ms for your message to reach me.')

@bot.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit = amount+1)

@bot.command(aliases=['Anime','rec','anime'])
async def recommend(ctx):
    my_url = 'https://myanimelist.net/anime/genre/8/Drama'
    uClient = urlopen(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = BeautifulSoup(page_html,'html.parser')
    container = page_soup.findAll('div',{'class':'title'})
    image = page_soup.findAll('div',{'class':'image'})
    i = random.choice(range(100))
    await ctx.send('My anime recommendation link:\n' +container[i].p.a['href'])
    await ctx.send(image[i].a.img['data-src'])

@bot.command(aliases=['Film','film'])
async def FILM(ctx):
    my_url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
    uClient = urlopen(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = BeautifulSoup(page_html,'html.parser')
    container = page_soup.findAll('td',{'class':'posterColumn'})
    i = random.choice(range(100))
    await ctx.send("My film recommendation is:\n"+container[i].a.img['alt'])

"""Not completed XO AI(Using MinMax) 😙
@bot.command(aliases = ["xo","xo_AI","XO_AI"])
async def game(ctx):
    await ctx.send("X-O game has started!")
    game_on = True
    EMPTY = None
    board = [[EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY]]
    
    while game_on == True:
        pv = ""
        pd = ""
        win_count_hor = 0
        win_count_dia = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == pv and board[i][j] != EMPTY:
                    win_count_hor += 1
                    if win_count_hor == 2:
                        await ctx.send(f'{pd} is the winner')
                        game_on = False
                else:
                    win_count = 0
                pv = board[i][j]
                if board[j][i] == pd and board[j][i] != EMPTY:
                    win_count_dia += 1
                    if win_count_dia == 2:
                        await ctx.send(f'{pv} is the winner')
                        game_on = False
                else:
                    win_count_dia = 0
                pd = board[j][i]
        if board[0][0] == board[1][1] == board[2][2] != EMPTY or board[0][2] == board[1][1] == board[2][0] != EMPTY:
            return board[1][1]
        
        await ctx.send(f"{board[0][0]} | {board[0][1]} | {board[0][2]}\n{board[1][0]} | {board[1][1]} | {board[1][2]}\n{board[2][0]} | {board[2][1]} | {board[2][2]}")
        nm = 0
        turn = ''
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    nm += 1
        if nm%2 == 0:
            turn = "O"
        else: 
            turn = "X"
        await ctx.send(f"{turn}'s turn")
        coor = await bot.wait_for('message', timeout=30)
        if coor == '1':
            board[0][0] = turn
        elif coor == '2':
            board[0][1] = turn
        elif coor == '3':
            board[0][2] = turn
        elif coor == '4':
            board[1][0] = turn
        elif coor == '5':
            board[1][1] = turn
        elif coor == '6':
            board[1][2] = turn
        elif coor == '7':
            board[2][0] = turn
        elif coor == '8':
            board[2][1] = turn
        elif coor == '9':
            board[2][2] = turn
"""
#just for fun commands:
@bot.command()
async def password(ctx):
    s = ['running','sleeping','silly','adventurous','smiling','monotonous']
    b = ['bee','guy','cat','naruto','innocent','monkey','scientist']
    m = []
    for i in range(100):
        m.append(i)
    await ctx.send(f"Your password is:\n {random.choice(s)+random.choice(b)+str(random.choice(m))}")

@bot.command()
async def pepo(ctx):
    e48=['https://tenor.com/view/goose-peepo-quack-pepe-the-frog-waddling-gif-17946795',
    'https://tenor.com/view/pepe-the-frof-peepo-wine-gif-16652751',
    'https://tenor.com/view/peepo-run-pepe-the-frog-gif-17317943',
    'https://tenor.com/view/peepo-arrive-peepo-pepe-the-frog-happy-gif-16095288',
    'https://tenor.com/view/peepo-smash-pepe-pepe-the-frog-punch-gif-16142453',
    'https://tenor.com/view/pepega-pls-xqc-dance-pepega-dance-pepe-pls-pepega-gif-16147647',
    'https://tenor.com/view/pepega-pepe-the-frog-gun-shooting-gif-16396270']
    await ctx.send(f'peeeeeepooo: {random.choice(e48)}')

@bot.command()
async def user_input(ctx):
    await ctx.send("INput")
    s = bot.wait_for('message',timeout=30)
    print(s)
bot.run('')# pass you bot token
