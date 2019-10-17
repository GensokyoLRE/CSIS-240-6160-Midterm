"""
Objective: Convert number from base-10/decimal to base-2/binary.
Restrictions:
    Only use binary addition/subtraction.
    Use whole # addition/subtraction (to validate?).
    Use recursion.
"""


class BinaryDecCalc:

    def dec_to_bin(self, in_dec):
        binary_link_circuit = []

        div_num = in_dec // 2
        div_rem = in_dec - (div_num * 2)

        binary_link_circuit.append(div_rem)

        if div_num == 0:
            return binary_link_circuit
        else:
            return self.dec_to_bin(div_num)

    @staticmethod
    def bin_to_dec(in_bin):
        """
        Split the binary (i.e. 11011 (decimal: 27)) into a list:
        list_blah = [1,1,0,1,1] //len = 5, index form 0 - 4
        Powers: [2^0, 2^1, 2^2, etc...]
        Index: [0, 1, 2, etc...]
        """
        str_in_bin = str(in_bin)
        list_bin = [int(x) for x in str_in_bin]
        dec_total = 0

        for i in range(len(list_bin)):
            """
            Backwards of list_bin
            
            Add 2^i "index" if binary is 1 in the slot, else ignore.
            """
            if list_bin[i] == 1:
                dec_total += 2^i
        return dec_total

    @staticmethod
    def bin_calc_add(bin_num_1, bin_num_2):
        """
        Do addition based on given binary.
        """
        list_bin_1 = [int(y) for y in str(bin_num_1)]
        list_bin_2 = [int(z) for z in str(bin_num_2)]
        list_bin_res = []
        carryover = 0

        """
        Do binary "addition"
        Binary 11 = Dec 3
        Binary 10 = Dec 2
        Binary 01 = Dec 1
        Binary 00 = Dec 0
        
        Current code example:
        list_bin_2 = [1,0,1,1,0]
        list_bin_1 = [0,1,1,1,1]
        
        Loop 1: 0 + 1 + 0 = 1
        append 1, carry 0
        L2: 1 + 1 + 0 = 2
        append 0, carry 1
        L3: 1 + 1 + 1 = 3
        append 1, carry 1
        L4: 0 + 1 + 1 = 2
        append 0, carry 1
        L5: 1 + 0 + 1 = 2
        append 0, carry 1
        max len reached, if carry = 1, append 1
        """
        while len(list_bin_2) > len(list_bin_1):
            list_bin_1.append(0)

        for i in reversed(range(len(list_bin_2))):
            bin_pseudo_total = list_bin_2[i] + list_bin_1[i] + carryover
            if bin_pseudo_total == 3:
                carryover = 1
                list_bin_res.append(1)
            elif bin_pseudo_total == 2:
                carryover = 1
                list_bin_res.append(0)
            else:
                list_bin_res.append(bin_pseudo_total)

        if carryover == 1:
            list_bin_res.append(1)
        return list_bin_res

    def bin_calc_sub(self, bin_num_1, bin_num_2):
        """
        Subtraction based on given binary.
        """
        str_bin_1 = str(bin_num_1)
        str_bin_2 = str(bin_num_2)
        rev = True

        list_bin_1 = [int(y) for y in str_bin_1]
        list_bin_2 = [int(z) for z in str_bin_2]
        list_bin_res = []

        while len(list_bin_2) > len(list_bin_1):
            list_bin_1.append(0)

        """
        If bpt = (0 + 0) - 1 = -1, borrow from next index, then add 2 to bpt
        If bpt = (1 + 0) - 1 = 0, append 0
        If bpt = (1 + 1) - 1 = 1, append 1
        """

        for i in reversed(range(len(list_bin_2))):
            if self.bin_to_dec(bin_num_1) > self.bin_to_dec(bin_num_2):
                bin_pseudo_total = list_bin_1[i] - list_bin_2[i]
                rev = False
            else:
                bin_pseudo_total = list_bin_2[i] - list_bin_1[i]
            if bin_pseudo_total <= -1:
                if rev:
                    list_bin_2[i + 1] -= 1
                else:
                    list_bin_1[i + 1] -= 1
                bin_pseudo_total += 2

            if bin_pseudo_total == 0:
                list_bin_res.append(0)
            elif bin_pseudo_total == 1:
                list_bin_res.append(1)

        return list_bin_res

    @staticmethod
    def whole_add(in_dec_1, in_dec_2):
        return in_dec_1 + in_dec_2

    @staticmethod
    def whole_sub(in_dec_1, in_dec_2):
        return (in_dec_1 - in_dec_2) if (in_dec_1 > in_dec_2) else (in_dec_2 - in_dec_1)


if __name__ == '__main__':
    bdc = BinaryDecCalc()
    running = True
    dialogue_menu = "Please select a menu option:\n" \
                    "1: Binary to decimal\n" \
                    "2: Decimal to binary\n" \
                    "3: Binary Addition\n" \
                    "4: Binary subtraction\n" \
                    "5: Whole Addition\n" \
                    "6: Whole Subtraction\n" \
                    "7: Exit\n" \
                    "Select: "
    
    while running:
        user_sel = int(input(dialogue_menu))
        while (0 >= user_sel) or (user_sel > 7):
            user_sel = int(input("ERROR: Wrong entry, please try again.\n"
                                 "Select: "))
        
        if user_sel == 1:
            bin_conv = int(input("WARNING: NO VALIDATION; PLEASE FOLLOW INSTRUCTION\n"
                                                "Please enter a binary value: "))
            dec_conv = bdc.bin_to_dec(bin_conv)
            print(f"User Binary Input: {bin_conv}\n"
                  f"Decimal Result: {dec_conv}")
        elif user_sel == 2:
            dec_conv = int(input("WARNING: NO VALIDATION; PLEASE FOLLOW INSTRUCTION\n"
                                 "Please enter a binary value: "))
            bin_conv = bdc.dec_to_bin(dec_conv)
            print(f"User Decimal Input: {dec_conv}\n"
                  f"Binary Result: {bin_conv}")
        elif (user_sel == 3) or (user_sel == 4):
            user_bin_calc_1 = int(input("WARNinG: NO VALIDATION; PLEASE FOLLOW INSTRUCTION\n"
                                       "Please enter a binary value: "))
            user_bin_calc_2 = int(input("WARNING: NO VALIDATION; PLEASE FOLLOW INSTRUCTION\n"
                                       "Please enter a secondary binary value: "))

            if user_sel == 3:
                bin_calc = bdc.bin_calc_add(user_bin_calc_1, user_bin_calc_2)
            else:
                bin_calc = bdc.bin_calc_sub(user_bin_calc_1, user_bin_calc_2)

            print(f"User Binary Inputs:\n"
                  f"{user_bin_calc_1}\n"
                  f"{user_bin_calc_2}\n"
                  f"Binary Result:\n"
                  f"{bin_calc}")

        elif (user_sel == 5) or (user_sel == 6):
            user_dec_calc_1 = int(input("WARNiNG: NO VALIDATION; PLEASE FOLLOW INSTRUCTION\n"
                                        "Please enter a decimal value: "))
            user_dec_calc_2 = int(input("WARNiNG: NO VALIDATION; PLEASE FOLLOW INSTRUCTION\n"
                                        "Please enter a secondary decimal value: "))

            if user_sel == 5:
                dec_calc = bdc.whole_add(user_dec_calc_1, user_dec_calc_2)
            else:
                dec_calc = bdc.whole_sub(user_dec_calc_1, user_dec_calc_2)

            print(f"User Binary Inputs:\n"
                  f"{user_dec_calc_1}\n"
                  f"{user_dec_calc_2}\n"
                  f"Binary Result:\n"
                  f"{dec_calc}")

        else:
            print("Exiting: Thank you for your time!")
            running = False
