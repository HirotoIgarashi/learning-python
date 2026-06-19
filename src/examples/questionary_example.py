import questionary


def main():
    # ユーザに提示する選択肢のリスト
    choices = [
        "Python (パイソン)",
        "JavaScript (ジャバスクリプト)",
        "Go (ゴー)",
        "Rust (ラスト)",
        "終了する",
    ]

    # 選択プロンプトの表示
    selected = questionary.select(
        "開発に使用したいプログラミング言語を選択してください:", choices=choices
    ).ask()

    # 選択結果に応じた処理
    if selected == "終了する":
        print("プログラムを終了します。")
    else:
        print(f"「{selected}」が選択されました！")


if __name__ == "__main__":
    main()
