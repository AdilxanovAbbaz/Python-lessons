from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("8052593935:AAGDugllAbO5347v3ihUZVp3nHGfRGdC9yw")  # Bot toekn
ADMINS = env.list("7625864389")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
