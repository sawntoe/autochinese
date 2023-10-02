from chinese_english_lookup import Dictionary
from chinese_english_lookup.dictionary import DefinitionEntry
import autopinyin, automarkdown
 
d = Dictionary()
words = open("words.txt", "r").readlines()

outfile = open("words.md", "w+")

entries = [["Word", "Pinyin", "English definition"]]

for word in words:
    if word == '\n':
        continue
    entry = d.lookup(word)
        
    entries.append([entry.simp, '<br><br>'.join(autopinyin.decode_pinyin(i.pinyin) for i in entry.definition_entries), '<br><br>'.join(' / '.join(i.definitions) for i in entry.definition_entries)])

outfile.write(automarkdown.make_markdown_table(entries))
