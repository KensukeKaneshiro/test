import PySimpleGUI as sg
import gui
import deepl


def main():    
    # 最初に表示するウィンドウを指定する。
    window = gui.main_window()
    # deepLの使用量を取得し、ウィンドウに表示させる。
    gui.get_usage(window)

    while True:
        event, values = window.read()
        if event == '-run_deepl-':
            message = values['-original_text-']

            # 翻訳先の言語を設定
            lng = deepl.lang_set(message)
            # DeepL翻訳実行
            trans_result = deepl.translate(message, t_lang=lng)
            # ウィンドウに翻訳結果を反映させる
            window['-translated_text-'].print(trans_result)

            # deepLの使用量を取得し、ウィンドウに表示させる。
            gui.get_usage(window)

        if event == sg.WIN_CLOSED or event == "Exit":
            break

    window.close()


if __name__ == '__main__':
    main()