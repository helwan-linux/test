# main.py

import sys
import typer
from hpm.cli import app as cli_app, print_custom_help, current_lang
from hpm.utils.early_args_patch import patch_args

def main():
    # الخطوة 1: معالجة الوسائط المبكرة
    detected_lang = patch_args()

    # الخطوة 2: التحقق مما إذا كان المستخدم يطلب المساعدة
    if "--help" in sys.argv:
        # طباعة المساعدة المخصصة بلغتها فقط
        print_custom_help(detected_lang or current_lang)
        sys.exit(0)

    # الخطوة 3: تشغيل التطبيق
    cli_app()

if __name__ == "__main__":
    main()
