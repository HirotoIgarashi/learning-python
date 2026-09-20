import os


def get_current_directory():
    """カレントディレクトリを文字列で返す"""
    return os.getcwd()


def change_current_directory(path):
    if is_dir_exists(path):
        os.chdir(path)
        return True
    else:
        return False


def create_directory(path):
    """与えられたpathを作成する"""
    if is_dir_exists(path):
        print("与えられたpathは既に存在しています。")
    else:
        os.mkdir(path)
        if is_dir_exists(path):
            return True
        else:
            return False


def remove_directory(path):
    """与えられたpathを削除する"""
    if is_dir_exists(path):
        os.rmdir(path)
        return True
    else:
        print("与えられたpathは存在していません。")
        return False


def is_dir_exists(path):
    """与えられたpathが存在してディレクトリであればTrueを返す"""
    return os.path.exists(path) & os.path.isdir(path)
