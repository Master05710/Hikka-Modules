import httpx
from telethon import types
from .. import loader, utils  # type: ignore

@loader.tds
class AIToolsMod(loader.Module):
    "Module for Hikka designed to work with Stable Diffusion: XL and GPT neural networks. Created by @TheXAiChannel"
    strings = {
        "name": "AITools",
        "processing": "<b>Processing request...</b>",
        "gpt_result": "<b>User request🤓:</b> <i>{}</i>\n<b>GPT response🤖:</b> <i>{}</i>",
        "done": "<b>Done! Your image:</b>",
        "sdxl_caption": "<b>Your image based on the request:</b> <i>{}</i>",
    }

    @loader.owner
    async def gptcmd(self, m: types.Message):
        ".gpt <text> - Send a request to GPT"
        args = utils.get_args_raw(m)
        m = await utils.answer(m, self.strings("processing", m))
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post("https://opo.monster/private/apis/gpt", json={"prompt": args})
            data = resp.text
            await utils.answer(m, self.strings("gpt_result", m).format(args, data))

    @loader.owner
    async def sdxlcmd(self, m: types.Message):
        ".sdxl <text> - Send a request to SDXL"
        args = utils.get_args_raw(m)
        m = await utils.answer(m, self.strings("processing", m))
        async with httpx.AsyncClient(timeout=120.0) as client:
            resp = await client.post("https://opo.monster/private/apis/sdxl", json={"prompt": args})
            data = resp.text
            await utils.answer(m, self.strings("done", m))
            await m.reply(file=data, message=self.strings("sdxl_caption", m).format(args))
