import random

# ３つのリストを作成する。動詞のリスト、形容詞のリスト、そして名詞のリスト
verbs = [
    "Leverage",
    "Sync",
    "Target",
    "Gamify",
    "Offline",
    "Crowd-sourced",
    "24/7",
    "Lean-in",
    "30,000 foot",
]
adjectives = [
    "A/B Tested",
    "Freemium",
    "Hyperlocal",
    "Siloed",
    "B-to-B",
    "Oriented",
    "Cloud-based",
    "API-based",
]
nouns = [
    "Early Adopter",
    "Low-hanging Fruit",
    "Pipeline",
    "Splash Page",
    "Productivity",
    "process",
    "Tipping Point",
    "Paradigm",
]

# リストから動詞、形容詞、名詞をそれぞれ１つ選ぶ
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

# 単語を「つなぎ合わせて」フレーズを作る
phrase = verb + " " + adjective + " " + noun

# フレーズを出力する
print(phrase)
