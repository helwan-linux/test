# hpm/i18n.py

LANGUAGES = {
    "en": {
        "description": "hpm: A simple and powerful package manager for Arch Linux.",
        "usage": "Usage",
        "dry_run_warning": "Running in dry-run mode. No changes will be made to the system.",
        "commands_title": "[bold blue]Available Commands[/bold blue]",
        "command_header": "Command",
        "description_header": "Description",
        "global_options_title": "Options",
        "dry_run_help": "Show what would be done without making any changes.",
        "lang_help": "Set the interface language.",
        "help_help": "Show this message and exit.",
        "commands": {
            "install": {"name": "install", "desc": "Installs one or more packages.", "aliases": ["i"]},
            "remove": {"name": "remove", "desc": "Removes a package.", "aliases": ["r"]},
            "upgrade": {"name": "upgrade", "desc": "Upgrades all installed packages.", "aliases": ["u"]},
            "refresh": {"name": "refresh", "desc": "Synchronizes databases and upgrades packages.", "aliases": ["s"]},
            "search": {"name": "search", "desc": "Searches for packages.", "aliases": ["q"]},
            "info": {"name": "info", "desc": "Displays detailed package info.", "aliases": ["I"]},
            "list": {"name": "list", "desc": "Lists all installed packages.", "aliases": ["l"]},
            "clean": {"name": "clean", "desc": "Cleans the package cache.", "aliases": ["c"]},
            "orphans": {"name": "orphans", "desc": "Manages orphan packages.", "aliases": ["o"]},
            "aur": {"name": "aur", "desc": "Manages packages from the AUR.", "aliases": ["a"]},
            "doctor": {"name": "doctor", "desc": "Performs a system health check.", "aliases": ["d"]},
            "history": {"name": "history", "desc": "Displays command history.", "aliases": ["h"]}
        }
    },
    "zh": {  # Chinese (Simplified)
        "description": "hpm: 一个简单而强大的 Arch Linux 包管理器。",
        "usage": "用法",
        "dry_run_warning": "在空运行模式下运行。系统将不会进行任何更改。",
        "commands_title": "[bold blue]可用命令[/bold blue]",
        "command_header": "命令",
        "description_header": "描述",
        "global_options_title": "选项",
        "dry_run_help": "显示将要执行的操作，但不做任何更改。",
        "lang_help": "设置界面语言。",
        "help_help": "显示此消息并退出。",
        "commands": {
            "install": {"name": "安装", "desc": "从仓库或本地文件安装一个或多个软件包。", "aliases": ["i"]},
            "remove": {"name": "卸载", "desc": "移除软件包及其不需要的依赖项。", "aliases": ["r"]},
            "upgrade": {"name": "升级", "desc": "将所有已安装的软件包升级到最新版本。", "aliases": ["u"]},
            "refresh": {"name": "刷新", "desc": "同步数据库并升级所有已安装的软件包。", "aliases": ["s"]},
            "search": {"name": "搜索", "desc": "在仓库中搜索软件包。", "aliases": ["q"]},
            "info": {"name": "信息", "desc": "显示一个或多个软件包的详细信息。", "aliases": ["I"]},
            "list": {"name": "列表", "desc": "列出所有已安装的软件包。", "aliases": ["l"]},
            "clean": {"name": "清理", "desc": "清理软件包缓存。", "aliases": ["c"]},
            "orphans": {"name": "孤儿", "desc": "管理孤儿软件包。", "aliases": ["o"]},
            "aur": {"name": "AUR", "desc": "管理 AUR 软件包。", "aliases": ["a"]},
            "doctor": {"name": "诊断", "desc": "执行系统健康检查。", "aliases": ["d"]},
            "history": {"name": "历史", "desc": "显示命令历史记录。", "aliases": ["h"]}
        }
    },
    "es": {  # Spanish
        "description": "hpm: Un gestor de paquetes simple y potente para Arch Linux.",
        "usage": "Uso",
        "dry_run_warning": "Ejecutando en modo de prueba. No se realizarán cambios en el sistema.",
        "commands_title": "[bold blue]Comandos Disponibles[/bold blue]",
        "command_header": "Comando",
        "description_header": "Descripción",
        "global_options_title": "Opciones",
        "dry_run_help": "Muestra lo que se haría sin realizar cambios.",
        "lang_help": "Establecer el idioma de la interfaz.",
        "help_help": "Mostrar este mensaje y salir.",
        "commands": {
            "install": {"name": "instalar", "desc": "Instala uno o más paquetes desde los repositorios o un archivo local.", "aliases": ["i"]},
            "remove": {"name": "eliminar", "desc": "Elimina un paquete y sus dependencias no necesarias.", "aliases": ["r"]},
            "upgrade": {"name": "actualizar", "desc": "Actualiza todos los paquetes instalados a la última versión.", "aliases": ["u"]},
            "refresh": {"name": "sincronizar", "desc": "Sincroniza las bases de datos y actualiza todos los paquetes instalados.", "aliases": ["s"]},
            "search": {"name": "buscar", "desc": "Busca paquetes en los repositorios.", "aliases": ["q"]},
            "info": {"name": "informacion", "desc": "Muestra información detallada sobre uno o más paquetes.", "aliases": ["I"]},
            "list": {"name": "lista", "desc": "Enumera todos los paquetes instalados.", "aliases": ["l"]},
            "clean": {"name": "limpiar", "desc": "Limpia la caché de paquetes.", "aliases": ["c"]},
            "orphans": {"name": "huerfanos", "desc": "Gestiona paquetes huérfanos.", "aliases": ["o"]},
            "aur": {"name": "aur", "desc": "Gestiona paquetes de AUR.", "aliases": ["a"]},
            "doctor": {"name": "diagnostico", "desc": "Realiza una comprobación del estado del sistema.", "aliases": ["d"]},
            "history": {"name": "historial", "desc": "Muestra el historial de comandos.", "aliases": ["h"]}
        }
    },
    "ar": {  # Arabic
        "description": "hpm: مدير حزم بسيط وقوي لـ Arch Linux.",
        "usage": "الاستخدام",
        "dry_run_warning": "يعمل في وضع التجربة. لن يتم إجراء أي تغييرات على النظام.",
        "commands_title": "[bold blue]الأوامر المتاحة[/bold blue]",
        "command_header": "الأمر",
        "description_header": "الوصف",
        "global_options_title": "الخيارات",
        "dry_run_help": "يعرض ما سيتم تنفيذه دون إجراء أي تغييرات.",
        "lang_help": "يضبط لغة الواجهة.",
        "help_help": "يعرض هذه الرسالة ويخرج.",
        "commands": {
            "install": {"name": "تثبيت", "desc": "يثبت حزمة واحدة أو أكثر.", "aliases": ["i"]},
            "remove": {"name": "إزالة", "desc": "يزيل حزمة.", "aliases": ["r"]},
            "upgrade": {"name": "ترقية", "desc": "يرقي جميع الحزم المثبتة.", "aliases": ["u"]},
            "refresh": {"name": "تحديث", "desc": "يزامن قواعد البيانات ويرقي الحزم.", "aliases": ["s"]},
            "search": {"name": "بحث", "desc": "يبحث عن حزم.", "aliases": ["q"]},
            "info": {"name": "معلومات", "desc": "يعرض معلومات مفصلة عن الحزمة.", "aliases": ["I"]},
            "list": {"name": "قائمة", "desc": "يسرد جميع الحزم المثبتة.", "aliases": ["l"]},
            "clean": {"name": "تنظيف", "desc": "ينظف ذاكرة التخزين المؤقت للحزم.", "aliases": ["c"]},
            "orphans": {"name": "يتيم", "desc": "يدير الحزم اليتيمة.", "aliases": ["o"]},
            "aur": {"name": "aur", "desc": "يدير حزم من Arch User Repository (AUR).", "aliases": ["a"]},
            "doctor": {"name": "فحص", "desc": "يقوم بفحص كامل لصحة النظام.", "aliases": ["d"]},
            "history": {"name": "سجل", "desc": "يعرض سجل الأوامر.", "aliases": ["h"]}
        }
    }
}

def get_translation(lang: str):
    """Retrieves a translation getter function for a given language."""
    if lang not in LANGUAGES:
        lang = "en"
    
    translations = LANGUAGES[lang]
    def translate(key: str):
        if key in translations:
            return translations[key]
        return LANGUAGES["en"][key]
    
    return translate

def get_full_translation_dict(lang: str):
    """Retrieves the full translation dictionary for a given language."""
    return LANGUAGES.get(lang, LANGUAGES["en"])
