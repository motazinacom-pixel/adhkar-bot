from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes, WebhookSettings
)
import random

# أذكار عامة
adhkar_general = [
    "سبحان الله وبحمده، سبحان الله العظيم",
    "لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير",
    "اللهم صل وسلم على نبينا محمد",
    "لا حول ولا قوة إلا بالله",
    "أستغفر الله العظيم وأتوب إليه",
    "حسبي الله لا إله إلا هو عليه توكلت وهو رب العرش العظيم",
    "اللهم اغفر لي ولوالدي وللمؤمنين يوم يقوم الحساب",
    "اللهم إني أعوذ بك من الهم والحزن، وأعوذ بك من العجز والكسل",
    "اللهم إني أعوذ بك من جهد البلاء، ودرك الشقاء، وسوء القضاء، وشماتة الأعداء"
]

# أذكار الصباح
adhkar_sabah = [
    "1. أصبحنا وأصبح الملك لله، والحمد لله...",
    "2. اللهم بك أصبحنا وبك أمسينا وبك نحيا وبك نموت وإليك النشور.",
    "3. رضيت بالله رباً وبالإسلام ديناً وبمحمد ﷺ نبياً.",
    "4. اللهم ما أصبح بي من نعمة أو بأحد من خلقك فمنك وحدك...",
    "5. اللهم عافني في بدني، عافني في سمعي، عافني في بصري...",
    "6. اللهم إني أسألك العفو والعافية في الدنيا والآخرة.",
    "7. اللهم استر عوراتي وآمن روعاتي..."
]

# أذكار المساء
adhkar_masaa = [
    "1. أمسينا وأمسى الملك لله، والحمد لله...",
    "2. اللهم بك أمسينا وبك أصبحنا وبك نحيا وبك نموت وإليك المصير.",
    "3. اللهم ما أمسى بي من نعمة أو بأحد من خلقك فمنك وحدك...",
    "4. أعوذ بكلمات الله التامات من شر ما خلق.",
    "5. اللهم إني أمسيت أشهدك وأشهد حملة عرشك...",
    "6. اللهم إني أعوذ بك من الهم والحزن...",
    "7. اللهم إني أعوذ بك من جهد البلاء..."
]

# أذكار النوم
adhkar_sleep = [
    "1. بِاسْمِكَ اللّهُمَّ أَمُوتُ وَأَحْيَا.",
    "2. اللهم قِني عذابك يوم تبعث عبادك.",
    "3. اللهم باسمك وضعت جنبي وبك أرفعه...",
    "4. اللهم أسلمت نفسي إليك، وفوضت أمري إليك...",
    "5. سبحان الله (٣٣)، الحمد لله (٣٣)، الله أكبر (٣٤)."
]

# سورة الملك كاملة مرقمة
sura_al_mulk = """📖 سورة الملك كاملة:

1. تبارك الذي بيده الملك وهو على كل شيء قدير  
2. الذي خلق الموت والحياة ليبلوكم أيكم أحسن عملا وهو العزيز الغفور  
3. الذي خلق سبع سماوات طباقا...  
4. ثم ارجع البصر كرتين ينقلب إليك البصر خاسئا وهو حسير  
5. ولقد زينا السماء الدنيا بمصابيح وجعلناها رجوما للشياطين...  
6. وللذين كفروا بربهم عذاب جهنم وبئس المصير  
7. إذا ألقوا فيها سمعوا لها شهيقا وهي تفور  
8. تكاد تميز من الغيظ...  
9. قالوا بلى قد جاءنا نذير فكذبنا...  
10. وقالوا لو كنا نسمع أو نعقل ما كنا...  
11. فاعترفوا بذنبهم فسحقا لأصحاب السعير  
12. إن الذين يخشون ربهم بالغيب لهم مغفرة وأجر كبير  
13. وأسروا قولكم أو اجهروا به...  
14. ألا يعلم من خلق وهو اللطيف الخبير  
15. هو الذي جعل لكم الأرض ذلولا...  
16. أأمنتم من في السماء أن يخسف بكم الأرض...  
17. أم أمنتم من في السماء أن يرسل عليكم حاصبا...  
18. ولقد كذب الذين من قبلهم فكيف كان نكير  
19. أولم يروا إلى الطير فوقهم صافات ويقبضن...  
20. أمن هذا الذي هو جند لكم ينصركم من دون الرحمن...  
21. أمن هذا الذي يرزقكم إن أمسك رزقه...  
22. أفمن يمشي مكبا على وجهه أهدى...  
23. قل هو الذي أنشأكم وجعل لكم السمع...  
24. قل هو الذي ذرأكم في الأرض...  
25. ويقولون متى هذا الوعد إن كنتم صادقين  
26. قل إنما العلم عند الله...  
27. فلما رأوه زلفة سيئت وجوه الذين كفروا...  
28. قل أرأيتم إن أهلكني الله ومن معي أو رحمنا...  
29. قل هو الرحمن آمنا به وعليه توكلنا...  
30. قل أرأيتم إن أصبح ماؤكم غورا فمن يأتيكم بماء معين
"""

# دالة /start
async def start(update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📖 سورة الملك", callback_data='mulk')],
        [InlineKeyboardButton("☀️ أذكار الصباح", callback_data='sabah')],
        [InlineKeyboardButton("🌙 أذكار المساء", callback_data='masaa')],
        [InlineKeyboardButton("🕊️ ذكر عشوائي", callback_data='random')],
        [InlineKeyboardButton("😴 أذكار النوم", callback_data='sleep')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("اختر من القائمة:", reply_markup=reply_markup)

# دالة الأزرار
async def button_handler(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'mulk':
        await query.edit_message_text(sura_al_mulk)
    elif data == 'sabah':
        await query.edit_message_text("☀️ أذكار الصباح:\n" + "\n".join(adhkar_sabah))
    elif data == 'masaa':
        await query.edit_message_text("🌙 أذكار المساء:\n" + "\n".join(adhkar_masaa))
    elif data == 'sleep':
        await query.edit_message_text("😴 أذكار النوم:\n" + "\n".join(adhkar_sleep))
    elif data == 'random':
        await query.edit_message_text("🕊️ ذكر عشوائي:\n" + random.choice(adhkar_general))

# تشغيل البوت
app = ApplicationBuilder().token("8406504256:AAFFZBPEgVzblybO6psClaGinF4JbXGMFnA").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

# إعداد Webhook باسم التطبيق الجديد
app.run_webhook(
    webhook_settings=WebhookSettings(
        listen="0.0.0.0",
        port=10000,
        webhook_url="https://adhkat-bot-4.onrender.com"
    )
)