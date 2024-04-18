import telegram
from telegram import _update
from telegram.ext import CommandHandler,MessageHandler,filters,ApplicationBuilder,CallbackQueryHandler,CallbackContext
# بناء البوت عن طريق التوكن الخاص به
البوت=ApplicationBuilder().token("6946080050:AAEXMlcOiVrLie4cj2Mb-N3S-9WAbxQjhB4").build()
# إنشاء دالة البوت وتحديد ARGs لإرسال الرسائل والحصول على معلومات المستخدم
async def start(update:_update,context:CallbackContext):
    #متغير لجلب معلومات المستخدم
    المستخدم=update.effective_user
    #الحصول على معلومات المستخدم وإرسال رسالة البدء عند الضغت على start
    await context.bot.send_message(chat_id=المستخدم.id, text="مرحبا بك في البوت,قم بإدخال العملية الحسابية")
async  def calculation(update:_update,context:CallbackContext):
    try:
        نص_الرسالة=update.message.text
        المستخدم=update.effective_user
        النتيجة=eval(نص_الرسالة)
    except:
        النتيجة="error"
    await context.bot.send_message(chat_id=المستخدم.id, text="النتيجة هي "+str(النتيجة))
print("جاري تشغيل البوت")
#تحديد أمر start لتشغيل البوت وأمر calculation للحساب
البوت.add_handler(CommandHandler("start",start))
البوت.add_handler(MessageHandler(filters.TEXT,calculation))
البوت.run_polling()
