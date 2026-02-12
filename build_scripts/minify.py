import os
import re


def minify_js(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Prosta minifikacja: usuwanie komentarzy i nowych linii
    content = re.sub(r'//.*', '', content)
    content = content.replace('\n', ' ').replace('\r', '')
    content = re.sub(r'\s+', ' ', content)

    output_path = file_path.replace('.js', '.min.js')
    with open(output_path, 'w') as f:
        f.write(content)
    print(f"Zminifikowano: {output_path}")


if __name__ == "__main__":
    minify_js('../frontend/script.js')