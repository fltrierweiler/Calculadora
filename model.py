

class Model():
    def __init__(self):
        self.value = ''
        self.operator = ''
        self.previous_value = ''

    def calculate(self, caption):
        if caption == 'C':
            self.value = ''
            self.previous_value = ''
            self.operator = ''

        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
        
        elif caption == '.':
            if not caption in self.value:
                self.value += caption
        
        elif caption == '%':
            value = float(self.value) if '.' in self.value else int(self.value)
            self.value = str(value/100)

        elif caption == '=':
            value = self._evaluate()

            if '.0' in str(value): # Converte resultado em número inteiro caso termine em .0
                value = int(value)
                
            self.value = str(value)
        
        elif isinstance(caption, int):
            self.value += str(caption)
        
        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ''

        return self.value

    def _evaluate(self):
        return eval(self.previous_value+self.operator+self.value)