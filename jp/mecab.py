import MeCab

tagger = MeCab.Tagger("-Owakati")

print(tagger.parse("pythonが大好きです").split())
