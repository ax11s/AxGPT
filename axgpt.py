import openai
from discord.ext import commands, tasks
import discord
from dataclasses import dataclass

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

BOT_TOKEN = ""

openai.api_key = ""
conversation = []



def generate_response(prompt):
  model_engine = "text-davinci-003"

  completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      temperature=0.5,
  )

  response = completions.choices[0].text
  return response




@bot.command()
async def chat(ctx, *, message):
    user_input = message
    conversation.append(user_input)
    prompt = "\n".join(conversation)
    response = generate_response(prompt)
    await ctx.send(f'{response}')
    conversation.append(response)

bot.run(BOT_TOKEN)
