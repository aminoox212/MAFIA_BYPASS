import os
import shutil

def main():
    file_name = "models.py"
    key_file = "KEY.txt"
    destination_path = "/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(current_dir, file_name)
    key_path = os.path.join(current_dir, key_file)

    # التحقق من وجود الملفات
    if not os.path.exists(source_path):
        print(f"File '{file_name}' not found.")
        return

    if not os.path.exists(key_path):
        print(f"File '{key_file}' not found.")
        return

    try:
        # قراءة المفتاح من KEY.txt
        with open(key_path, "r") as kf:
            key = kf.read().strip()

        # استبدال @@@@ بالمفتاح
        with open(source_path, "r") as file:
            content = file.read()
        modified_content = content.replace("@@@@", key)

        # كتابة الملف المعدل
        with open(source_path, "w") as file:
            file.write(modified_content)

        # نسخ الملف إلى مكتبة requests
        os.makedirs(destination_path, exist_ok=True)
        shutil.copy(source_path, destination_path)

        # استرجاع المحتوى الأصلي للملف
        restored_content = modified_content.replace(key, "@@@@")
        with open(source_path, "w") as file:
            file.write(restored_content)

        print("Mafia tool bypassed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()