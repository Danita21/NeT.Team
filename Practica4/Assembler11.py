class Assembler:
    def __init__(self):
        self.symbol_table = self.create_symbol_table()
        self.variable_address = 16  # La memoria para variables empieza en la dirección 16
    
    def create_symbol_table(self):
        symbols = {
            "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4, "R0": 0, "R1": 1,
            "R2": 2, "R3": 3, "R4": 4, "R5": 5, "R6": 6, "R7": 7, "R8": 8,
            "R9": 9, "R10": 10, "R11": 11, "R12": 12, "R13": 13, "R14": 14,
            "R15": 15, "SCREEN": 16384, "KBD": 24576
        }
        return symbols

    def parse(self, input_file):
        with open(input_file, 'r') as file:
            instructions = file.readlines()
        instructions = self.first_pass(instructions)
        binary_code = self.second_pass(instructions)
        return binary_code
    
    def first_pass(self, instructions):
        rom_address = 0
        processed_instructions = []
        for line in instructions:
            line = line.split('//')[0].strip()
            if not line:
                continue
            if line.startswith('(') and line.endswith(')'):
                label = line[1:-1]
                self.symbol_table[label] = rom_address
            else:
                processed_instructions.append(line)
                rom_address += 1
        return processed_instructions

    def second_pass(self, instructions):
        binary_code = []
        for instruction in instructions:
            if instruction.startswith('@'):
                binary_code.append(self.translate_a_instruction(instruction))
            else:
                binary_code.append(self.translate_c_instruction(instruction))
        return binary_code

    def translate_a_instruction(self, instruction):
        value = instruction[1:]
        if value.isdigit():
            address = int(value)
        else:
            if value not in self.symbol_table:
                self.symbol_table[value] = self.variable_address
                self.variable_address += 1
            address = self.symbol_table[value]
        return f"{address:016b}"

    def translate_c_instruction(self, instruction):
        dest, comp, jump = None, None, None
        if '=' in instruction:
            dest, instruction = instruction.split('=')
        if ';' in instruction:
            comp, jump = instruction.split(';')
        else:
            comp = instruction
        comp_bits = self.comp_to_bin(comp)
        dest_bits = self.dest_to_bin(dest)
        jump_bits = self.jump_to_bin(jump)
        return f"111{comp_bits}{dest_bits}{jump_bits}"
    
    def comp_to_bin(self, comp):
        comp_table = {
            "0": "0101010", "1": "0111111", "-1": "0111010", "D": "0001100",
            "A": "0110000", "!D": "0001101", "!A": "0110001", "-D": "0001111",
            "-A": "0110011", "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
            "A-1": "0110010", "D+A": "0000010", "D-A": "0010011", "A-D": "0000111",
            "D&A": "0000000", "D|A": "0010101", "M": "1110000", "!M": "1110001",
            "-M": "1110011", "M+1": "1110111", "M-1": "1110010", "D+M": "1000010",
            "D-M": "1010011", "M-D": "1000111", "D&M": "1000000", "D|M": "1010101"
        }
        return comp_table[comp]
    
    def dest_to_bin(self, dest):
        dest_table = {
            None: "000", "M": "001", "D": "010", "MD": "011", "A": "100",
            "AM": "101", "AD": "110", "AMD": "111"
        }
        return dest_table[dest]
    
    def jump_to_bin(self, jump):
        jump_table = {
            None: "000", "JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100",
            "JNE": "101", "JLE": "110", "JMP": "111"
        }
        return jump_table[jump]


def main():
    assembler = Assembler()
    binary_code = assembler.parse('Add.asm')
    with open('Add.hack', 'w') as file:
        for line in binary_code:
            file.write(line + '\n')


if __name__ == "__main__":
    main()

 
 