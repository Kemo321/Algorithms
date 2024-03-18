class File:
    def __init__(self, filename: str) -> None:
        self._filename = filename

    def write_text(self, text: list) -> None:
        with open(self._filename, 'w', encoding='utf-8') as handle:
            for i in range(len(text)):
                handle.write(f'{text[i]} ')
                if (i + 1) % 8 == 0:
                    handle.write('\n')

    def load_text(self, test="") -> list:
        text = []
        with open(self._filename, 'r', encoding='utf-8') as handle:
            for line in handle:
                line = line.strip()
                line = line.split()
                for word in line:
                    try:
                        word = word.lower()
                        text.append(word)
                    # only want to sort words containing latin alphabet letters
                    except Exception:
                        pass
        return text

    def set_filename(self, filename: str) -> None:
        self._filename = filename
