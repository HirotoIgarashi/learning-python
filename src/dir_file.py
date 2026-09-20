from module import direcotry_module as dir

# カレントディレクトリパスを取得する
# Print Current Working Directory
courrent_directory = dir.get_current_directory()
print("courrent_directory: " + courrent_directory)

directory_to_create = courrent_directory + "/testDir"

# Current DirectoryにtestDirが存在するかをチェクする。存在していれば
# ディレクトリかどうかをチェックする。存在しているというメッセージを表示する。
# 存在していなければtestDirの ディレクトリを作成する
print(directory_to_create + "を作成します。")
dir.create_directory(directory_to_create)

# カレントディレクトリの変更
# Change Current Directory
# os.chdir("testDir")
dir.change_current_directory("testDir")

# ディレクトリ名を変更する
# ディレクトリを削除する
print(directory_to_create + "を削除します。")
dir.remove_directory(directory_to_create)

# カレントディレクトリを元に戻します
dir.change_current_directory("..")

# courrent_directory = os.getcwd()
courrent_directory = dir.get_current_directory()
print("courrent_directory: " + courrent_directory)


# ファイルを作成する
# ファイルを読み込む
# ファイルを更新する
# ファイルを削除する
