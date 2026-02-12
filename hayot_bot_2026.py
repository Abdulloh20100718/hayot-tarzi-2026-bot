import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime, timedelta
import json
import threading
import time

# ============================================
# 🌟 TOKEN - @HayotTarzi2026Bot
# ============================================
TOKEN = "8209052337:AAF811UfqiSi-7uFYC-VVHl7tZvEQofxKro"
bot = telebot.TeleBot(TOKEN)

# ============================================
# 💾 DATABASE
# ============================================
users_data = {}

# ============================================
# 🌙 RAMAZON 2026 - TO'LIQ 29 KUN TAQVIMI
# ============================================
RAMAZON_2026 = {
    "2026-02-19": {
        "kun": 1, "bomdod": "05:57", "saharlik": "07:13", 
        "peshin": "12:37", "asr": "16:19", "shom": "18:07", 
        "xufton": "19:18", "tahajjud": "02:00",
        "duo": "Allohumma laka sumtu va bika aamantu va 'alayka tavakkaltu",
        "hadis": "Ro'za tutgan kishining xursandchiligi ikki: iftor vaqti va Robbisi bilan uchrashganda",
        "fazilat": "Ramazon oyi - Qur'on nozil bo'lgan oy"
    },
    "2026-02-20": {
        "kun": 2, "bomdod": "05:55", "saharlik": "07:11", 
        "peshin": "12:37", "asr": "16:20", "shom": "18:08", 
        "xufton": "19:19", "tahajjud": "01:59",
        "duo": "Rabbana atina fid-dunya hasanatan va fil-akhirati hasanatan",
        "hadis": "Kim Ramazon oyida imon bilan va savob umidida ro'za tutsa, o'tgan gunohlari kechiriladi",
        "fazilat": "Ramazon - saxovat va karam oyi"
    },
    "2026-02-21": {
        "kun": 3, "bomdod": "05:54", "saharlik": "07:10", 
        "peshin": "12:37", "asr": "16:21", "shom": "18:09", 
        "xufton": "19:20", "tahajjud": "01:59",
        "duo": "Rabbighfir li va li vaalidayya",
        "hadis": "Ro'zador uchun ikki sevinc bor: iftor vaqti va ro'zaning savobi beriladigan vaqt",
        "fazilat": "Ramazon - rahmat oyi"
    },
    "2026-02-22": {
        "kun": 4, "bomdod": "05:53", "saharlik": "07:09", 
        "peshin": "12:37", "asr": "16:22", "shom": "18:10", 
        "xufton": "19:21", "tahajjud": "01:58",
        "duo": "Allohumma innaka 'afuvvun tuhibbul 'afva fa'fu 'anni",
        "hadis": "Ro'za - qalqon, u bilan gunohlardan saqlaning",
        "fazilat": "Ramazon - mag'firat oyi"
    },
    "2026-02-23": {
        "kun": 5, "bomdod": "05:51", "saharlik": "07:07", 
        "peshin": "12:36", "asr": "16:23", "shom": "18:11", 
        "xufton": "19:22", "tahajjud": "01:57",
        "duo": "Subhanallahi va bihamdihi, subhanallahil 'azim",
        "hadis": "Jannatda Rayyon eshigi bor, undan faqat ro'zadorlar kiradi",
        "fazilat": "Ramazon - Qur'on oyi"
    },
    "2026-02-24": {
        "kun": 6, "bomdod": "05:50", "saharlik": "07:06", 
        "peshin": "12:36", "asr": "16:24", "shom": "18:13", 
        "xufton": "19:24", "tahajjud": "01:57",
        "duo": "Allohumma salli 'ala Muhammadin",
        "hadis": "Ro'za va Qur'on banda uchun shafoatchi bo'ladi",
        "fazilat": "Ramazon - duo qabul bo'ladigan oy"
    },
    "2026-02-25": {
        "kun": 7, "bomdod": "05:48", "saharlik": "07:04", 
        "peshin": "12:36", "asr": "16:25", "shom": "18:14", 
        "xufton": "19:25", "tahajjud": "01:56",
        "duo": "La ilaha illallahu vahdahu la sharika lah",
        "hadis": "Saharlik yengil bo'lsa ham barakotli",
        "fazilat": "Ramazon - baraka oyi"
    },
    "2026-02-26": {
        "kun": 8, "bomdod": "05:47", "saharlik": "07:03", 
        "peshin": "12:36", "asr": "16:26", "shom": "18:15", 
        "xufton": "19:26", "tahajjud": "01:56",
        "duo": "Astag'firullohal 'azimal-lazi la ilaha illa huwal hayyul qayyum",
        "hadis": "Iftorda duolar ijobat bo'ladi",
        "fazilat": "Ramazon - kechirilish oyi"
    },
    "2026-02-27": {
        "kun": 9, "bomdod": "05:45", "saharlik": "07:01", 
        "peshin": "12:36", "asr": "16:27", "shom": "18:16", 
        "xufton": "19:27", "tahajjud": "01:55",
        "duo": "Allohumma ajirni minan-nar",
        "hadis": "Kim Ramazon oyida bir kun ro'za tutsa, Jahannamdan 70 yil masofa uzoqlashadi",
        "fazilat": "Ramazon - najot oyi"
    },
    "2026-02-28": {
        "kun": 10, "bomdod": "05:44", "saharlik": "07:00", 
        "peshin": "12:36", "asr": "16:28", "shom": "18:17", 
        "xufton": "19:28", "tahajjud": "01:55",
        "duo": "Rabbana taqabbal minna innaka antas-sami'ul 'alim",
        "hadis": "Ro'zador iftorda xursand bo'ladi",
        "fazilat": "Ramazon - birinchi o'n kunlik - rahmat"
    },
    "2026-03-01": {
        "kun": 11, "bomdod": "05:42", "saharlik": "06:58", 
        "peshin": "12:35", "asr": "16:29", "shom": "18:19", 
        "xufton": "19:29", "tahajjud": "01:54",
        "duo": "Allohumma innaka 'afuvvun",
        "hadis": "Sadaqa ro'zaning aybini ketkazadi",
        "fazilat": "Ramazon - saxovat oyi"
    },
    "2026-03-02": {
        "kun": 12, "bomdod": "05:41", "saharlik": "06:57", 
        "peshin": "12:35", "asr": "16:30", "shom": "18:20", 
        "xufton": "19:30", "tahajjud": "01:54",
        "duo": "Rabbana hab lana min azvajina va zurriyyatina qurrata a'yun",
        "hadis": "Ro'za - sabrning yarmi",
        "fazilat": "Ramazon - Qur'on oyi"
    },
    "2026-03-03": {
        "kun": 13, "bomdod": "05:39", "saharlik": "06:55", 
        "peshin": "12:35", "asr": "16:31", "shom": "18:21", 
        "xufton": "19:31", "tahajjud": "01:53",
        "duo": "Allohumma ahyina bil iman",
        "hadis": "Ro'za va namoz banda uchun nurdir",
        "fazilat": "Ramazon - duo oyi"
    },
    "2026-03-04": {
        "kun": 14, "bomdod": "05:38", "saharlik": "06:53", 
        "peshin": "12:35", "asr": "16:32", "shom": "18:22", 
        "xufton": "19:33", "tahajjud": "01:52",
        "duo": "Rabbana la tuzig qulubana",
        "hadis": "Kim yolg'on so'zni tark etmasa, Allohga ro'zasini tark etishi kerak emas",
        "fazilat": "Ramazon - tarbiya oyi"
    },
    "2026-03-05": {
        "kun": 15, "bomdod": "05:36", "saharlik": "06:52", 
        "peshin": "12:35", "asr": "16:33", "shom": "18:23", 
        "xufton": "19:34", "tahajjud": "01:51",
        "duo": "Allohumma ihdina",
        "hadis": "Ro'za sabrning yarmidir",
        "fazilat": "Ramazon - o'rta o'n kunlik - mag'firat"
    },
    "2026-03-06": {
        "kun": 16, "bomdod": "05:35", "saharlik": "06:50", 
        "peshin": "12:34", "asr": "16:34", "shom": "18:24", 
        "xufton": "19:35", "tahajjud": "01:51",
        "duo": "Subhanallah",
        "hadis": "Kim ro'za tutib, iftorda 'Allohumma laka sumtu' desa, farishtalar duo qiladi",
        "fazilat": "Ramazon - ibodat oyi"
    },
    "2026-03-07": {
        "kun": 17, "bomdod": "05:33", "saharlik": "06:49", 
        "peshin": "12:34", "asr": "16:35", "shom": "18:25", 
        "xufton": "19:36", "tahajjud": "01:50",
        "duo": "Alhamdulillah",
        "hadis": "Saharlik vaqtida duo ijobat bo'ladi",
        "fazilat": "Ramazon - baraka oyi"
    },
    "2026-03-08": {
        "kun": 18, "bomdod": "05:31", "saharlik": "06:47", 
        "peshin": "12:34", "asr": "16:36", "shom": "18:27", 
        "xufton": "19:37", "tahajjud": "01:49",
        "duo": "Allohu Akbar",
        "hadis": "Ro'zador uchun ikki xursandchilik",
        "fazilat": "Ramazon - najot oyi"
    },
    "2026-03-09": {
        "kun": 19, "bomdod": "05:30", "saharlik": "06:45", 
        "peshin": "12:34", "asr": "16:37", "shom": "18:28", 
        "xufton": "19:38", "tahajjud": "01:49",
        "duo": "La hawla wa la quwwata illa billah",
        "hadis": "Ramazon - sabr oyi",
        "fazilat": "Ramazon - Qadr kechasi"
    },
    "2026-03-10": {
        "kun": 20, "bomdod": "05:28", "saharlik": "06:44", 
        "peshin": "12:33", "asr": "16:38", "shom": "18:29", 
        "xufton": "19:39", "tahajjud": "01:48",
        "duo": "Allohummaftahli abvaba rahmatik",
        "hadis": "Kim Ramazonda imon va savob umidida tursa, o'tgan gunohlari kechiriladi",
        "fazilat": "Ramazon - Qadr kechasini qidirish"
    },
    "2026-03-11": {
        "kun": 21, "bomdod": "05:27", "saharlik": "06:42", 
        "peshin": "12:33", "asr": "16:39", "shom": "18:30", 
        "xufton": "19:41", "tahajjud": "01:48",
        "duo": "Allohumma innaka 'afuvvun tuhibbul 'afva fa'fu 'anni",
        "hadis": "Qadr kechasini oxirgi o'n kunda qidiring",
        "fazilat": "Ramazon - Qadr kechasi"
    },
    "2026-03-12": {
        "kun": 22, "bomdod": "05:25", "saharlik": "06:40", 
        "peshin": "12:33", "asr": "16:40", "shom": "18:31", 
        "xufton": "19:42", "tahajjud": "01:47",
        "duo": "Rabbana atina fid-dunya hasanah",
        "hadis": "Qadr kechasi ming oydan yaxshiroq",
        "fazilat": "Ramazon - oxirgi o'n kunlik - do'zaxdan ozod qilish"
    },
    "2026-03-13": {
        "kun": 23, "bomdod": "05:23", "saharlik": "06:39", 
        "peshin": "12:33", "asr": "16:41", "shom": "18:32", 
        "xufton": "19:43", "tahajjud": "01:46",
        "duo": "Rabbana ghfir lana",
        "hadis": "Kim Qadr kechasini ibodat bilan o'tkazsa, o'tgan gunohlari kechiriladi",
        "fazilat": "Ramazon - Qadr kechasi"
    },
    "2026-03-14": {
        "kun": 24, "bomdod": "05:21", "saharlik": "06:37", 
        "peshin": "12:32", "asr": "16:42", "shom": "18:33", 
        "xufton": "19:44", "tahajjud": "01:45",
        "duo": "Allohumma a'inni 'ala zikrika",
        "hadis": "Ro'za - qalqon",
        "fazilat": "Ramazon - itikaf"
    },
    "2026-03-15": {
        "kun": 25, "bomdod": "05:20", "saharlik": "06:35", 
        "peshin": "12:32", "asr": "16:43", "shom": "18:34", 
        "xufton": "19:45", "tahajjud": "01:44",
        "duo": "Rabbana zalamna anfusana",
        "hadis": "Saharlik barakotdir",
        "fazilat": "Ramazon - oxirgi o'n kun"
    },
    "2026-03-16": {
        "kun": 26, "bomdod": "05:18", "saharlik": "06:34", 
        "peshin": "12:32", "asr": "16:43", "shom": "18:36", 
        "xufton": "19:46", "tahajjud": "01:44",
        "duo": "Allohumma inni as'alukal jannah",
        "hadis": "Ro'za va Qur'on shafoatchi",
        "fazilat": "Ramazon - duo kechalari"
    },
    "2026-03-17": {
        "kun": 27, "bomdod": "05:16", "saharlik": "06:32", 
        "peshin": "12:32", "asr": "16:44", "shom": "18:37", 
        "xufton": "19:48", "tahajjud": "01:43",
        "duo": "Allohumma ajirni minan-nar",
        "hadis": "Qadr kechasi 27-kun bo'lishi mumkin",
        "fazilat": "Ramazon - Qadr kechasi"
    },
    "2026-03-18": {
        "kun": 28, "bomdod": "05:15", "saharlik": "06:30", 
        "peshin": "12:31", "asr": "16:45", "shom": "18:38", 
        "xufton": "19:49", "tahajjud": "01:42",
        "duo": "Rabbana atmim lana nurana",
        "hadis": "Kim Ramazon oyida bir farzni bajo keltirsa, boshqa oylarda 70 farz bajo keltirgandek",
        "fazilat": "Ramazon - kechirilish"
    },
    "2026-03-19": {
        "kun": 29, "bomdod": "05:13", "saharlik": "06:29", 
        "peshin": "12:31", "asr": "16:46", "shom": "18:39", 
        "xufton": "19:50", "tahajjud": "01:41",
        "duo": "Alhamdulillahillazi balag'ana Ramazon",
        "hadis": "Ro'za va Qadr kechasi har bir ummatga berilmagan",
        "fazilat": "Ramazon - bayram"
    }
}

# ============================================
# 📚 9 TA FAN VIDEO DARSLAR
# ============================================
SUBJECT_VIDEOS = {
    "📐 Matematika": {
        "title": "📐 MATEMATIKA - Usmonov kurslari",
        "url": "https://youtube.com/@matematikakursi",
        "description": "✅ Eng sara matematika darslari\n🎯 Kirish imtihoniga tayyorlov\n🔥 500+ video darslar"
    },
    "⚛️ Fizika": {
        "title": "⚛️ FIZIKA - Kirish imtihoni",
        "url": "https://youtu.be/oxoBvF7j8JA",
        "description": "✅ Fizika fanidan maxsus tayyorlov\n🎯 Masalalar yechimi\n🔥 Video darslik"
    },
    "🇬🇧 Ingliz tili": {
        "title": "🇬🇧 INGLIZ TILI - IELTS/General",
        "url": "https://youtu.be/W2cw-k2UoP8?list=PLilzkXdXk5udVe9t9RSOeqKDSvt5Mfcsa",
        "description": "✅ Ingliz tili grammatikasi\n🎯 IELTS tayyorlov\n🔥 To'liq playlist"
    },
    "🧪 Kimyo": {
        "title": "🧪 KIMYO - Organik/Anorganik",
        "url": "https://youtu.be/ONroxVLyrDs?list=PLp2s3iqJuT2ijOFSYgdhMNk7uT9oKfxbk",
        "description": "✅ Kimyo fanidan video darslar\n🎯 Masalalar yechimi\n🔥 Playlist"
    },
    "🧬 Biologiya": {
        "title": "🧬 BIOLOGIYA - 11-sinf",
        "url": "https://youtube.com/results?search_query=biologiya+11+sinf",
        "description": "✅ Biologiya fanidan tayyorlov\n🎯 Testlar tahlili\n🔥 Video darslar"
    },
    "📖 Ona tili": {
        "title": "📖 ONA TILI - Grammatika",
        "url": "https://youtu.be/2mciwEz_S3Q?list=PLOLz2vuEAiKITDc_1I8lMnSrvBSY6LFh5",
        "description": "✅ Ona tili qoidalari\n🎯 Imlo va grammatika\n🔥 To'liq kurs"
    },
    "📚 Adabiyot": {
        "title": "📚 ADABIYOT - Asarlar tahlili",
        "url": "https://youtu.be/ODIAkLSdwv8?list=PLOLz2vuEAiKIXmZ-GnWIpElQW1ijl0Wjp",
        "description": "✅ Adabiyot fanidan darslar\n🎯 Asarlar tahlili\n🔥 Yozuvchilar hayoti"
    },
    "🧠 Tarix": {
        "title": "🧠 TARIX - Jahon/O'zbekiston",
        "url": "https://youtu.be/4jh5iWJ7Cds?list=PLOLz2vuEAiKKaLFjU_r3oBWarzSW5mgyY",
        "description": "✅ Tarix fanidan video darslar\n🎯 Sanalar va voqealar\n🔥 To'liq playlist"
    },
    "🇷🇺 Rus tili": {
        "title": "🇷🇺 RUS TILI - Grammatika",
        "url": "https://youtu.be/NubrWHBh4O0?list=PLkREkayoYCyKU9nkSEzZXtg0XudlQ7tKM",
        "description": "✅ Rus tili grammatikasi\n🎯 So'z boyligi\n🔥 Video darslar"
    }
}

# ============================================
# 👤 FOYDALANUVCHI MA'LUMOTLARI
# ============================================
def get_user_data(user_id):
    if user_id not in users_data:
        users_data[user_id] = {
            "name": "",
            "level": 1,
            "xp": 0,
            "achievements": [],
            "ramazon": {
                "roza": {},  # kun: True/False
                "iftar": {},
                "tarawih": {},
                "streak": 0,
                "total": 0
            },
            "created": datetime.now().strftime("%Y-%m-%d")
        }
    return users_data[user_id]

def save_user_data(user_id, data):
    users_data[user_id] = data

def is_ramazon():
    today = datetime.now().strftime("%Y-%m-%d")
    return today in RAMAZON_2026

def get_today_ramazon():
    today = datetime.now().strftime("%Y-%m-%d")
    return RAMAZON_2026.get(today, None)

# ============================================
# 🏠 START KOMANDASI
# ============================================
@bot.message_handler(commands=['start'])
def start(message):
    user_id = str(message.chat.id)
    user_data = get_user_data(user_id)
    user_name = message.from_user.first_name
    
    if not user_data["name"]:
        user_data["name"] = user_name
        save_user_data(user_id, user_data)
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("🌙 Ramazon 2026"),
        KeyboardButton("📺 Video darslar"),
        KeyboardButton("📊 Statistika"),
        KeyboardButton("🏆 Yutuqlar"),
        KeyboardButton("⚙️ Sozlamalar")
    )
    
    # Ramazon holati
    ramazon_text = ""
    if is_ramazon():
        ramazon = get_today_ramazon()
        kun = ramazon['kun']
        roza_holati = user_data["ramazon"]["roza"].get(datetime.now().strftime("%Y-%m-%d"), False)
        holat = "✅ Tutdingiz" if roza_holati else "❌ Tutmadingiz"
        ramazon_text = f"\n🌙 Ramazon {kun}-kun | {holat} | Iftar: {ramazon['shom']}"
    else:
        days_left = (datetime(2026, 2, 19) - datetime.now()).days
        ramazon_text = f"\n🌙 Ramazonga {days_left} kun qoldi"
    
    text = f"""
🌟 **HAYOT TARZI 2026** 🌟

👋 Assalomu alaykum, {user_data['name']}!

📅 {datetime.now().strftime('%d-%B %Y, %A')}
{ramazon_text}

🔥 Daraja: Level {user_data['level']} | XP: {user_data['xp']}/1000
🏆 Yutuqlar: {len(user_data['achievements'])} ta
🌙 Ramazon ro'za: {user_data['ramazon']['total']}/29 kun

👇 Quyidagilardan birini tanlang:
    """
    
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

# ============================================
# 🌙 RAMAZON 2026 - ASOSIY MENYU
# ============================================
@bot.message_handler(func=lambda message: message.text == "🌙 Ramazon 2026")
def ramazon_main_menu(message):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("📅 Bugungi Ramazon", callback_data="ramazon_today"),
        InlineKeyboardButton("🗓 To'liq taqvim", callback_data="ramazon_calendar"),
        InlineKeyboardButton("✅ Ro'za tutdim", callback_data="ramazon_roza_yes"),
        InlineKeyboardButton("❌ Tutmadim", callback_data="ramazon_roza_no"),
        InlineKeyboardButton("📊 Mening ro'zam", callback_data="ramazon_my_fasts"),
        InlineKeyboardButton("🏆 Ramazon yutuqlari", callback_data="ramazon_achievements"),
        InlineKeyboardButton("📖 Ramazon haqida", callback_data="ramazon_about")
    )
    
    text = """
🌙 **RAMAZON 2026** 🌙
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 19-Fevral — 19-Mart (29 kun)

🎯 **RAMAZON OYINING FAZILATLARI:**
✨ Qur'on nozil bo'lgan oy
✨ Ro'za islomning 5 ruknidan biri
✨ Qadr kechasi - 1000 oydan afzal
✨ Gunohlar kechiriladi
✨ Duolar ijobat bo'ladi

👇 Kerakli bo'limni tanlang:
    """
    
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

# ============================================
# 📅 BUGUNGI RAMAZON
# ============================================
def ramazon_today(call):
    user_id = str(call.message.chat.id)
    user_data = get_user_data(user_id)
    ramazon = get_today_ramazon()
    
    if not ramazon:
        days_left = (datetime(2026, 2, 19) - datetime.now()).days
        text = f"""
🌙 **RAMAZON 2026** 🌙
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 Hali Ramazon kelmagan!
⏳ {days_left} kun qoldi

📌 Boshlanishi: 19-Fevral 2026
📌 Tugashi: 19-Mart 2026

🎯 Ramazonga tayyorlaning!
        """
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=text,
            parse_mode="Markdown"
        )
        return
    
    kun = ramazon['kun']
    today = datetime.now().strftime("%Y-%m-%d")
    roza_tutdim = user_data["ramazon"]["roza"].get(today, False)
    iftar_qildim = user_data["ramazon"]["iftar"].get(today, False)
    tarawih_oqidim = user_data["ramazon"]["tarawih"].get(today, False)
    
    status_roza = "✅" if roza_tutdim else "❌"
    status_iftar = "✅" if iftar_qildim else "❌"
    status_tarawih = "✅" if tarawih_oqidim else "❌"
    
    progress = user_data['ramazon']['total'] * 100 // 29
    
    text = f"""
🌙 **RAMAZON 2026 — {kun}-KUN** 🌙
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 {datetime.now().strftime('%d-%B %Y')}

🕋 **BUGUNGI NAMOZ VAQTLARI:**
┌─────────────────────────┐
│ 🌅 Bomdod:    {ramazon['bomdod']}     │
│ 🌙 Saharlik:  {ramazon['saharlik']}   │
│ ☀️ Peshin:    {ramazon['peshin']}     │
│ 🌆 Asr:       {ramazon['asr']}        │
│ 🌇 Shom:      {ramazon['shom']}   ⭐  │
│ 🌃 Xufton:    {ramazon['xufton']}     │
│ 🌙 Tahajjud:  {ramazon['tahajjud']}   │
└─────────────────────────┘

📊 **HOZIRGI HOLATINGIZ:**
▫️ Ro'za: {status_roza} {roza_tutdim and "Tutdingiz" or "Tutmadingiz"}
▫️ Iftar: {status_iftar} {iftar_qildim and "Qildingiz" or "Qilmadingiz"}
▫️ Tarawih: {status_tarawih} {tarawih_oqidim and "O'qidingiz" or "O'qimadingiz"}

📈 **UMUMIY PROGRESS:**
[{('█' * (progress // 5))}{('░' * (20 - (progress // 5)))}] {progress}%
🎯 {user_data['ramazon']['total']}/29 kun

🤲 **BUGUNGI DUO:**
{ramazon['duo']}

📿 **BUGUNGI HADIS:**
{ramazon['hadis']}

💫 **BUGUNGI FAZILAT:**
{ramazon['fazilat']}
    """
    
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("✅ Ro'za tutdim", callback_data="ramazon_roza_yes"),
        InlineKeyboardButton("❌ Tutmadim", callback_data="ramazon_roza_no"),
        InlineKeyboardButton("✅ Iftar qildim", callback_data="ramazon_iftar_yes"),
        InlineKeyboardButton("❌ Qilmadim", callback_data="ramazon_iftar_no"),
        InlineKeyboardButton("✅ Tarawih o'qidim", callback_data="ramazon_tarawih_yes"),
        InlineKeyboardButton("❌ O'qimadim", callback_data="ramazon_tarawih_no"),
        InlineKeyboardButton("🔙 Orqaga", callback_data="ramazon_back")
    )
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        parse_mode="Markdown",
        reply_markup=markup
    )

# ============================================
# 🗓 TO'LIQ RAMAZON TAQVIMI
# ============================================
def ramazon_calendar(call):
    text = """
🗓 **RAMAZON 2026 TO'LIQ TAQVIMI** 🗓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 19-Fevral — 19-Mart 2026
"""
    
    markup = InlineKeyboardMarkup(row_width=3)
    
    # 29 kun uchun tugmalar
    for date, data in RAMAZON_2026.items():
        day = data['kun']
        date_show = date[-5:].replace("-", "/")  # 02/19 formatida
        markup.add(InlineKeyboardButton(
            f"{day}-kun ({date_show})", 
            callback_data=f"ramazon_day_{day}"
        ))
    
    markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="ramazon_back"))
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        parse_mode="Markdown",
        reply_markup=markup
    )

# ============================================
# 📆 KUNLIK RAMAZON MA'LUMOTLARI
# ============================================
def ramazon_day_info(call, day):
    # Kunni topish
    day_data = None
    for date, data in RAMAZON_2026.items():
        if data['kun'] == day:
            day_data = data
            date_str = date
            break
    
    if not day_data:
        return
    
    user_id = str(call.message.chat.id)
    user_data = get_user_data(user_id)
    
    roza_tutdim = user_data["ramazon"]["roza"].get(date_str, False)
    
    text = f"""
🗓 **RAMAZON {day}-KUN** 🗓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 {date_str}

🕋 **NAMOZ VAQTLARI:**
Bomdod: {day_data['bomdod']} | Saharlik: {day_data['saharlik']}
Peshin: {day_data['peshin']} | Asr: {day_data['asr']}
Shom: {day_data['shom']} ⭐ | Xufton: {day_data['xufton']}
Tahajjud: {day_data['tahajjud']}

📊 **HOLATINGIZ:**
Ro'za: {'✅ Tutgan' if roza_tutdim else '❌ Tutmagan'}

🤲 **DUO:**
{day_data['duo']}

📿 **HADIS:**
{day_data['hadis']}

💫 **FAZILAT:**
{day_data['fazilat']}
    """
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="ramazon_calendar"))
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        parse_mode="Markdown",
        reply_markup=markup
    )

# ============================================
# 📊 MENING RO'ZAM
# ============================================
def ramazon_my_fasts(call):
    user_id = str(call.message.chat.id)
    user_data = get_user_data(user_id)
    
    total = user_data['ramazon']['total']
    progress = total * 100 // 29
    
    text = f"""
📊 **MENING RO'ZAM** 📊
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 {user_data['name']}
🌙 Ramazon 2026

✅ **TUTGAN KUNLARIM:** {total}/29
❌ **TUTMAGAN KUNLARIM:** {29 - total}/29
📈 **PROGRESS:** {progress}%

📅 **KUNLAR BO'YICHA:**
    """
    
    # 29 kun bo'yicha ro'za holati
    for i in range(1, 30):
        kun_found = False
        for date, data in RAMAZON_2026.items():
            if data['kun'] == i:
                roza = user_data["ramazon"]["roza"].get(date, False)
                status = "✅" if roza else "⬜"
                text += f"\n{i:2d}-kun: {status}"
                kun_found = True
                break
        if not kun_found:
            text += f"\n{i:2d}-kun: ⬜"
    
    if total >= 29:
        text += "\n\n🏆 TABRIKLAYMAN! Siz Ramazon ro'zasini to'liq tutdingiz!"
    elif total >= 20:
        text += "\n\n💪 Zo'r! Ramazonning ko'p kunida ro'za tutdingiz!"
    elif total >= 10:
        text += "\n\n👍 Yaxshi! Davom ettiring!"
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="ramazon_back"))
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        parse_mode="Markdown",
        reply_markup=markup
    )

# ============================================
# 🏆 RAMAZON YUTUQLARI
# ============================================
def ramazon_achievements(call):
    user_id = str(call.message.chat.id)
    user_data = get_user_data(user_id)
    
    total = user_data['ramazon']['total']
    streak = user_data['ramazon']['streak']
    
    text = f"""
🏆 **RAMAZON YUTUQLARI** 🏆
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 {user_data['name']}
🌙 Ramazon 2026

📊 **STATISTIKA:**
✅ Umumiy ro'za: {total}/29 kun
🔥 Ketma-ket ro'za: {streak} kun

🎯 **YUTUQLAR:**
    """
    
    # 7 kun yutug'i
    if total >= 7:
        text += "\n✅ [7/7] Bir hafta ro'za - 100 XP"
    else:
        text += f"\n⬜ [7/7] Bir hafta ro'za - {total}/7 kun"
    
    # 15 kun yutug'i
    if total >= 15:
        text += "\n✅ [15/15] Yarim oy ro'za - 250 XP"
    else:
        text += f"\n⬜ [15/15] Yarim oy ro'za - {total}/15 kun"
    
    # 29 kun yutug'i
    if total >= 29:
        text += "\n✅ [29/29] To'liq Ramazon - 1000 XP 🏆"
    else:
        text += f"\n⬜ [29/29] To'liq Ramazon - {total}/29 kun"
    
    # Streak yutuqlari
    if streak >= 7:
        text += "\n✅ 7 kun ketma-ket ro'za - 150 XP"
    if streak >= 15:
        text += "\n✅ 15 kun ketma-ket ro'za - 300 XP"
    if streak >= 29:
        text += "\n✅ 29 kun ketma-ket ro'za - 1000 XP 🌟"
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="ramazon_back"))
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        parse_mode="Markdown",
        reply_markup=markup
    )

# ============================================
# 📖 RAMAZON HAQIDA
# ============================================
def ramazon_about(call):
    text = """
📖 **RAMAZON OYI HAQIDA** 📖
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌙 **RAMAZON NIMA?**
Ramazon - hijriy qamariy taqvimning 9-oyi. Bu oyda musulmonlar ro'za tutadilar.

📿 **RO'ZA NIMA?**
Ro'za - tong otishidan quyosh botguncha yeb-ichmaslik va jinsiy aloqadan tiyilish.

✨ **RAMAZON FAZILATLARI:**
1️⃣ Qur'oni Karim nozil qilingan oy
2️⃣ Ro'za islomning 5 ruknidan biri
3️⃣ Qadr kechasi - 1000 oydan afzal
4️⃣ Bu oyda shaytonlar kishanlanadi
5️⃣ Jannat eshiklari ochiladi, do'zax eshiklari yopiladi

🤲 **SAHARLIK DUOSI:**
"Navaytu an asuma sovma shahri ramazona minal fajri ilal mag'ribi, xolisan lillahi ta'ala"

🌅 **IFTOR DUOSI:**
"Allohumma laka sumtu va bika aamantu va 'alayka tavakkaltu va 'ala rizqika aftartu"

💎 **QADR KECHASI:**
Ramazonning oxirgi 10 kunida, ayniqsa toq kechalarida qidiriladi. Bu kecha 1000 oydan afzal.

🎯 **RAMAZON AMALLARI:**
• Ro'za tutish
• Tarawih namozi
• Qur'on o'qish
• Sadaqa berish
• Itikaf
• Duo qilish

📅 **2026 RAMAZON:**
19-Fevral — 19-Mart (29 kun)
    """
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="ramazon_back"))
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        parse_mode="Markdown",
        reply_markup=markup
    )

# ============================================
# 📺 VIDEO DARSLAR
# ============================================
@bot.message_handler(func=lambda message: message.text == "📺 Video darslar")
def video_menu(message):
    text = """
📺 **9 TA FAN BO'YICHA VIDEO DARSLAR** 📺
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Quyidagi fanlardan birini tanlang:
    """
    
    markup = InlineKeyboardMarkup(row_width=2)
    for subject, data in SUBJECT_VIDEOS.items():
        markup.add(InlineKeyboardButton(
            f"{subject}", 
            callback_data=f"video_{subject}"
        ))
    
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

# ============================================
# 📊 STATISTIKA
# ============================================
@bot.message_handler(func=lambda message: message.text == "📊 Statistika")
def statistics(message):
    user_id = str(message.chat.id)
    user_data = get_user_data(user_id)
    
    total_study = 0  # video darslar statistikasi
    ramazon_total = user_data['ramazon']['total']
    
    text = f"""
📊 **2026 YIL STATISTIKASI** 📊
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 **FOYDALANUVCHI:** {user_data['name']}
🔥 **DARAJANGIZ:** Level {user_data['level']} | XP: {user_data['xp']}/1000
📅 **BOSHLANGAN SANA:** {user_data['created']}

🌙 **RAMAZON 2026:**
✅ Ro'za tutgan: {ramazon_total}/29 kun
📈 Progress: {ramazon_total * 100 // 29}%
🔥 Ketma-ket: {user_data['ramazon']['streak']} kun

📚 **TA'LIM:**
📺 Video darslar: {total_study} ta
🎯 Maqsad: 365 kun

🏆 **YUTUQLAR:** {len(user_data['achievements'])} ta
    """
    
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# ============================================
# 🏆 YUTUQLAR
# ============================================
@bot.message_handler(func=lambda message: message.text == "🏆 Yutuqlar")
def achievements(message):
    user_id = str(message.chat.id)
    user_data = get_user_data(user_id)
    
    text = f"""
🏆 **YUTUQLAR GALEREYASI** 🏆
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 {user_data['name']}
🔥 Level {user_data['level']} | XP: {user_data['xp']}/1000
🌙 Ramazon ro'za: {user_data['ramazon']['total']}/29
    """
    
    if user_data['achievements']:
        text += "\n\n📋 **QO'LGA KIRITILGAN YUTUQLAR:**"
        for ach in user_data['achievements']:
            text += f"\n🏅 {ach}"
    else:
        text += "\n\n❌ Hali yutuqlar yo'q"
        text += "\n\n🎯 **YUTUQ OLISH UCHUN:**"
        text += "\n• 🌙 Ro'za tuting"
        text += "\n• 📺 Video darslar ko'ring"
        text += "\n• 🔥 7 kun ketma-ket ro'za tuting"
        text += "\n• 🏆 29 kun to'liq ro'za tuting"
    
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# ============================================
# ⚙️ SOZLAMALAR
# ============================================
@bot.message_handler(func=lambda message: message.text == "⚙️ Sozlamalar")
def settings(message):
    user_id = str(message.chat.id)
    user_data = get_user_data(user_id)
    
    text = f"""
⚙️ **SOZLAMALAR** ⚙️
━━━━━━━━━━━━━━━━━━━━━━━

🤖 **BOT MA'LUMOTLARI:**
📌 @HayotTarzi2026Bot
👤 Ismingiz: {user_data['name']}
📅 2026 - Hayot Tarzi
🌙 Ramazon 2026: 19-Fevral - 19-Mart
🎯 9 ta fan video darslari

📌 **BUYRUQLAR:**
/start - Botni qayta ishga tushirish
    """
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(
        KeyboardButton("🏠 Bosh sahifa")
    )
    
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

# ============================================
# 🏠 BOSH SAHIFA
# ============================================
@bot.message_handler(func=lambda message: message.text == "🏠 Bosh sahifa")
def home(message):
    start(message)

# ============================================
# 🔘 CALLBACK HANDLER - RAMAZON VA VIDEO
# ============================================
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = str(call.message.chat.id)
    user_data = get_user_data(user_id)
    
    try:
        # ========== RAMAZON MENYU ==========
        if call.data == "ramazon_today":
            ramazon_today(call)
        
        elif call.data == "ramazon_calendar":
            ramazon_calendar(call)
        
        elif call.data.startswith("ramazon_day_"):
            day = int(call.data.replace("ramazon_day_", ""))
            ramazon_day_info(call, day)
        
        elif call.data == "ramazon_my_fasts":
            ramazon_my_fasts(call)
        
        elif call.data == "ramazon_achievements":
            ramazon_achievements(call)
        
        elif call.data == "ramazon_about":
            ramazon_about(call)
        
        elif call.data == "ramazon_back":
            ramazon_main_menu(call.message)
        
        # ========== RAMAZON RO'ZA ==========
        elif call.data == "ramazon_roza_yes":
            today = datetime.now().strftime("%Y-%m-%d")
            if today in RAMAZON_2026:
                if not user_data["ramazon"]["roza"].get(today, False):
                    user_data["ramazon"]["roza"][today] = True
                    user_data["ramazon"]["total"] += 1
                    user_data["ramazon"]["streak"] += 1
                    user_data["xp"] += 50
                    
                    # 7 kun streak yutug'i
                    if user_data["ramazon"]["streak"] == 7:
                        user_data["achievements"].append("🔥 7 kun ketma-ket ro'za")
                        user_data["xp"] += 100
                        bot.answer_callback_query(call.id, "🏆 YUTUQ! 7 kun ketma-ket ro'za!", show_alert=True)
                    
                    # 29 kun to'liq yutug'i
                    if user_data["ramazon"]["total"] == 29:
                        user_data["achievements"].append("🌙 RAMAZON CHAMPIONI! 29/29 ro'za")
                        user_data["xp"] += 1000
                        user_data["level"] += 2
                        bot.answer_callback_query(call.id, "🏆 RAMAZON CHAMPIONI! +1000 XP", show_alert=True)
                    
                    save_user_data(user_id, user_data)
                    bot.answer_callback_query(call.id, "✅ Ro'za qabul qilindi! +50 XP")
                else:
                    bot.answer_callback_query(call.id, "✅ Siz allaqachon ro'za tutganingizni belgilagansiz!")
            
            ramazon_today(call)
        
        elif call.data == "ramazon_roza_no":
            today = datetime.now().strftime("%Y-%m-%d")
            if today in RAMAZON_2026:
                user_data["ramazon"]["roza"][today] = False
                user_data["ramazon"]["streak"] = 0
                save_user_data(user_id, user_data)
                bot.answer_callback_query(call.id, "❌ Belgilandi: Tutmadingiz")
            
            ramazon_today(call)
        
        elif call.data == "ramazon_iftar_yes":
            today = datetime.now().strftime("%Y-%m-%d")
            if today in RAMAZON_2026:
                user_data["ramazon"]["iftar"][today] = True
                user_data["xp"] += 25
                save_user_data(user_id, user_data)
                bot.answer_callback_query(call.id, "🌅 Iftar muborak! +25 XP")
            
            ramazon_today(call)
        
        elif call.data == "ramazon_iftar_no":
            today = datetime.now().strftime("%Y-%m-%d")
            if today in RAMAZON_2026:
                user_data["ramazon"]["iftar"][today] = False
                save_user_data(user_id, user_data)
                bot.answer_callback_query(call.id, "❌ Belgilandi")
            
            ramazon_today(call)
        
        elif call.data == "ramazon_tarawih_yes":
            today = datetime.now().strftime("%Y-%m-%d")
            if today in RAMAZON_2026:
                user_data["ramazon"]["tarawih"][today] = True
                user_data["xp"] += 30
                save_user_data(user_id, user_data)
                bot.answer_callback_query(call.id, "🕌 Tarawih o'qildi! +30 XP")
            
            ramazon_today(call)
        
        elif call.data == "ramazon_tarawih_no":
            today = datetime.now().strftime("%Y-%m-%d")
            if today in RAMAZON_2026:
                user_data["ramazon"]["tarawih"][today] = False
                save_user_data(user_id, user_data)
                bot.answer_callback_query(call.id, "❌ O'qilmadi")
            
            ramazon_today(call)
        
        # ========== VIDEO DARSLAR ==========
        elif call.data.startswith("video_"):
            subject = call.data.replace("video_", "")
            video_data = SUBJECT_VIDEOS.get(subject, {})
            
            user_data["xp"] += 10
            save_user_data(user_id, user_data)
            
            text = f"""
📺 **{video_data['title']}** 📺
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{video_data['description']}

🎬 **VIDEO DARSLIK:**
👉 [▶️ VIDEONI KO'RISH]({video_data['url']})

💡 **MASLAHAT:**
• Kuniga 30 daqiqa video ko'ring
• Muhim joylarni yozib oling
• Har kuni kamida 1 ta video

✨ **+10 XP!** (Jami: {user_data['xp']} XP)
            """
            
            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton("▶️ Videoni ko'rish", url=video_data['url']),
                InlineKeyboardButton("🔙 Orqaga", callback_data="back_to_videos")
            )
            
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=text,
                parse_mode="Markdown",
                reply_markup=markup,
                disable_web_page_preview=False
            )
        
        elif call.data == "back_to_videos":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            video_menu(call.message)
    
    except Exception as e:
        print(f"Callback xatolik: {e}")
        bot.answer_callback_query(call.id, "❌ Xatolik yuz berdi")

# ============================================
# 🚀 BOTNI ISHGA TUSHIRISH
# ============================================
if __name__ == "__main__":
    print("=" * 60)
    print("🌙 HAYOT TARZI 2026 BOT - RAMAZON TAQVIMI")
    print("=" * 60)
    print(f"🤖 Bot: @HayotTarzi2026Bot")
    print(f"🔑 Token: {TOKEN[:10]}...{TOKEN[-5:]}")
    print(f"🌙 Ramazon 2026: 19-Fevral - 19-Mart")
    print(f"📚 Fanlar: 9 ta video darslar")
    print(f"📅 Sana: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    print("✅ BOT ISHGA TUSHDI!")
    print("📱 Telegramda @HayotTarzi2026Bot ga /start yozing")
    print("=" * 60)
    
    # Botni ishga tushirish
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"❌ Xatolik: {e}")
            print("🔄 5 soniyadan keyin qayta uriniladi...")
            time.sleep(5)
            continue