from telethon import types
from .. import loader, utils  # type: ignore
import aitoolsAPI

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
        data = await aitoolsAPI.gpt(args)  # use your library to make the request
        await utils.answer(m, self.strings("gpt_result", m).format(args, data))

    @loader.owner
    async def sdxlcmd(self, m: types.Message):
        ".sdxl <text> - Send a request to SDXL"
        args = utils.get_args_raw(m)
        m = await utils.answer(m, self.strings("processing", m))
        data = await aitoolsAPI.sdxl(args)  # use your library to make the request
        await utils.answer(m, self.strings("done", m))
        await m.reply(file=data, message=self.strings("sdxl_caption", m).format(args))