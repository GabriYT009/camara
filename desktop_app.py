import os
import sys
import webview


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


def main():
    html_path = resource_path("index.html")

    if not os.path.exists(html_path):
        raise FileNotFoundError(f"No se encontró el archivo: {html_path}")

    url = "file://" + html_path.replace("\\", "/")

    webview.create_window(
        "Aula",
        url,
        width=1380,
        height=930,
        resizable=True,
        min_size=(1200, 780),
        fullscreen=False,
    )
    webview.start(debug=False, gui="windows")


if __name__ == "__main__":
    main()
