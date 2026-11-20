from html import escape
from time import time

from pyrogram.types import InputRichMessage

from ..core.telegram_manager import TgClient
from ..helper.ext_utils.bot_utils import new_task
from ..helper.telegram_helper.button_build import ButtonMaker
from ..helper.telegram_helper.message_utils import (
    send_message,
    edit_message,
    send_file,
    send_rich_message,
)
from ..helper.telegram_helper.filters import CustomFilters
from ..helper.telegram_helper.bot_commands import BotCommands


@new_task
async def start(_, message):
    buttons = ButtonMaker()
    buttons.url_button(
        "Repo", "https://github.com/itswill00/mirror-leech-telegram-bot"
    )
    buttons.url_button("Code Owner", "https://t.me/noticesa")
    reply_markup = buttons.build_menu(2)
    username = escape(TgClient.NAME or "mirrorax_bot")
    help_cmd = f"/{BotCommands.HelpCommand}"

    if await CustomFilters.authorized(_, message):
        title = "✨ Mirror & Leech"
        rich = (
            f"<h1>{title}</h1>"
            "<p>Mirror dan leech file dari link, Telegram, torrent, NZB, "
            "yt-dlp, dan gallery-dl.</p>"
            "<hr/>"
            "<h3>🚀 Yang bisa saya lakukan</h3>"
            "<p>📥 Mirror / leech • 🧲 Torrent • 🎬 yt-dlp • 🖼️ gallery-dl</p>"
            "<p>☁️ Upload ke GoFile, Telegram, atau rclone cloud</p>"
            "<hr/>"
            f"<aside>💡 Ketik <code>{help_cmd}</code> untuk daftar command. "
            "Untuk upload ke Telegram, gunakan <code>/leech</code>.</aside>"
            f"<footer>@{username}</footer>"
        )
        plain = (
            f"✨ <b>{title}</b>\n\n"
            "Mirror dan leech file dari link, Telegram, torrent, NZB, "
            "yt-dlp, dan gallery-dl.\n\n"
            "📥 Mirror / leech • 🧲 Torrent • 🎬 yt-dlp • 🖼️ gallery-dl\n"
            "☁️ Upload ke GoFile, Telegram, atau rclone cloud\n\n"
            f"💡 Ketik {help_cmd} untuk daftar command. "
            "Untuk upload ke Telegram, gunakan /leech."
        )
    else:
        title = "🔒 Mirror & Leech"
        rich = (
            f"<h1>{title}</h1>"
            "<p>Bot ini bisa mirror dari link, Telegram, torrent, NZB, "
            "dan media sosial ke cloud atau Telegram.</p>"
            "<blockquote>⚠️ Anda belum diizinkan. Minta owner mengirim "
            "<code>/auth</code> di grup ini.</blockquote>"
            f"<footer>@{username}</footer>"
        )
        plain = (
            f"🔒 <b>{title}</b>\n\n"
            "Bot ini bisa mirror dari link, Telegram, torrent, NZB, "
            "dan media sosial ke cloud atau Telegram.\n\n"
            "⚠️ Anda belum diizinkan. Minta owner mengirim /auth di grup ini."
        )

    result = await send_rich_message(
        message, InputRichMessage(html=rich), reply_markup, block=False
    )
    if isinstance(result, str):
        await send_message(message, plain, reply_markup)


@new_task
async def ping(_, message):
    start_time = int(round(time() * 1000))
    reply = await send_message(message, "Starting Ping")
    end_time = int(round(time() * 1000))
    await edit_message(reply, f"{end_time - start_time} ms")


@new_task
async def log(_, message):
    await send_file(message, "log.txt")
