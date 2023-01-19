import PySimpleGUI as sg # PySimpleGUIをインポート
import deepl # 自作のdeepl.pyをインポート

sg.theme('Reddit')

# メインウィンドウ
def main_window():
    layout = [
        [sg.Text('原文(日本語、英語翻訳)', size=(37, 2), justification='center'),   # ...①
         sg.Text('翻訳結果', size=(37, 2), justification='center')], #  ...② 
        [sg.Multiline('', key='-original_text-', size=(35, 10)),   # ...③
         sg.Multiline('', key='-translated_text-', size=(35, 10))],  # ...④ 
        [sg.Button('実行', size=(10, 1), key='-run_deepl-', pad=(100, 20))],  # ...⑤
        [sg.Text('DeepL使用量', size=(74, 1), justification='center')],  # ...⑥
        [sg.Text('',size=(74, 1), key='-Char_cnt-', justification='center')],  # ...⑦ 
    ]

    return sg.Window("翻訳アプリ", layout, finalize=True)

# DeepL使用率を取得し、Windowをアップデート
def get_usage(window):
    count_result = deepl.char_cnt()
    if count_result is None:
        sg.popup('APIキーを確認して下さい')
    else:
        count_used = count_result['character_count']
        count_limit = count_result['character_limit']
        bar_used = count_used / count_limit * 100
        output_txt = str(count_used) + ' / ' + str(count_limit) + '文字'
        window['-Char_cnt-'].update(output_txt)
