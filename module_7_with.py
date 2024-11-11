class WordsFinder:
    def __init__(self, *files: list):
        self.file_names = []
        for file_name in files:
            self.file_names.append(file_name)

    def get_all_words(self) -> dict:
        all_words = {}
        punctuation_syms = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                file_str = file.read()
                file_str = file_str.replace('\n', '')
                for replace_str in punctuation_syms:
                    file_str = file_str.replace(replace_str, ' ')
                file_str = (file_str.strip()).lower()
            all_words[file_name] = file_str.split(' ')
        return all_words

    def find(self, word: str) -> dict:
        find_dict = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    find_dict[name] = i + 1
                    break
        return find_dict

    def count(self, word: str) -> dict:
        find_dict = {}
        for name, words in self.get_all_words().items():
            found_cnt = 0
            for i in range(len(words)):
                if word.lower() == words[i]:
                    found_cnt += 1
            if found_cnt > 0:
                find_dict[name] = found_cnt
        return find_dict


finder2 = WordsFinder('test_file.txt', 'test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
