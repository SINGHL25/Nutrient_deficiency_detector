
from googletrans import Translator

translator = Translator()

def translate_text(text, target_lang='hi'):
    """
    Translate text into target_lang.
    Default: Hindi ('hi'). Use 'mr' for Marathi, 'en' for English.
    """
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Fallback to original text
