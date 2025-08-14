# hpm/utils/early_args_patch.py

import sys
from typing import Dict

HELP_ALIASES: Dict[str, str] = {
    "--ayuda": "es",
    "--帮助": "zh",
    "--مساعدة": "ar",
    "--lang": "en",
    "-h": "en",
    "--help": "en"
}

COMMAND_ALIASES: Dict[str, str] = {
    "es": {
        "instalar": "install", "i": "install",
        "eliminar": "remove", "r": "remove",
        "actualizar": "upgrade", "u": "upgrade",
        "sincronizar": "refresh", "s": "refresh",
        "buscar": "search", "q": "search",
        "informacion": "info", "I": "info",
        "lista": "list", "l": "list",
        "limpiar": "clean", "c": "clean",
        "huerfanos": "orphans", "o": "orphans",
        "aur": "aur", "a": "aur",
        "diagnostico": "doctor", "d": "doctor",
        "historial": "history", "h": "history"
    },
    "zh": {
        "安装": "install", "i": "install",
        "卸载": "remove", "r": "remove",
        "升级": "upgrade", "u": "upgrade",
        "刷新": "refresh", "s": "refresh",
        "搜索": "search", "q": "search",
        "信息": "info", "I": "info",
        "列表": "list", "l": "list",
        "清理": "clean", "c": "clean",
        "孤儿": "orphans", "o": "orphans",
        "AUR": "aur", "a": "aur",
        "诊断": "doctor", "d": "doctor",
        "历史": "history", "h": "history"
    },
    "ar": {
        "تثبيت": "install", "i": "install",
        "إزالة": "remove", "r": "remove",
        "ترقية": "upgrade", "u": "upgrade",
        "تحديث": "refresh", "s": "refresh",
        "بحث": "search", "q": "search",
        "معلومات": "info", "I": "info",
        "قائمة": "list", "l": "list",
        "تنظيف": "clean", "c": "clean",
        "يتيم": "orphans", "o": "orphans",
        "aur": "aur", "a": "aur",
        "فحص": "doctor", "d": "doctor",
        "سجل": "history", "h": "history"
    }
}

def patch_args():
    """
    Patches command-line arguments to handle localized commands and help flags.
    Returns the detected language code or None.
    """
    detected_lang = None
    new_args = []
    
    for arg in sys.argv[1:]:
        is_command = False
        
        for lang_code, aliases in COMMAND_ALIASES.items():
            if arg in aliases:
                new_args.append(aliases[arg])
                detected_lang = lang_code
                is_command = True
                break
        
        if arg in HELP_ALIASES:
            new_args.append("--help")
            detected_lang = HELP_ALIASES[arg]
            is_command = True

        if not is_command:
            new_args.append(arg)

    sys.argv = [sys.argv[0]] + new_args
    return detected_lang
