#✅ Flag tìm được là: .;,;.{imagine_if_i_made_it_compiled!!!}

from z3 import *

# Dùng BitVec thay vì Int để hỗ trợ bitwise
flag = [BitVec(f'c{i}', 8) for i in range(39)]
s = Solver()

# Giới hạn giá trị mỗi ký tự (ASCII printable)
for c in flag:
    s.add(c >= 32, c <= 126)

# Các điều kiện
s.add(flag[37] * flag[15] == 3366)
s.add(flag[8] + flag[21] == 197)
s.add(flag[8] * flag[13] == 9215)
s.add(flag[0] * flag[3] == 2714)
s.add(flag[3] + flag[21] == 159)
s.add(flag[1] * flag[20] == 5723)
s.add(flag[6] | flag[37] == 105)
s.add(flag[11] * flag[7] == 11990)
s.add(flag[29] & flag[25] == 100)
s.add(flag[16] | flag[29] == 127)
s.add(flag[20] - flag[6] == -8)
s.add(flag[21] + flag[20] == 197)
s.add(flag[2] + flag[36] == 77)
s.add(flag[35] * flag[11] == 3630)
s.add(flag[4] * flag[3] == 2714)
s.add(flag[35] ^ flag[6] == 72)
s.add(flag[25] + flag[24] == 221)
s.add(flag[14] * flag[36] == 3465)
s.add((flag[15] - flag[11]) - 148 == -156)
s.add(flag[37] + flag[17] == 138)
s.add(flag[1] ^ flag[38] == 70)
s.add(flag[9] + flag[29] == 212)
s.add(flag[30] - flag[10] == 7)
s.add(flag[10] + flag[33] == 206)
s.add(flag[7] * flag[15] == 11118)
s.add(flag[28] * flag[14] * 55 == 641025)
s.add((flag[7] | flag[4]) | 216 == 255)
s.add(flag[24] + flag[4] == 151)
s.add(flag[2] * flag[30] == 4928)
s.add(flag[5] + flag[22] == 224)
s.add(flag[18] | flag[36] == 127)
s.add(flag[13] + flag[34] == 195)
s.add(flag[9] | flag[17] == 111)
s.add(flag[12] * flag[9] == 10403)
s.add(flag[25] ^ flag[27] == 23)
s.add(flag[13] ^ flag[34] == 59)
s.add(flag[18] + flag[31] == 200)
s.add(flag[17] + flag[32] == 213)
s.add(flag[2] * flag[12] == 4444)
s.add(flag[24] * flag[31] == 11025)
s.add(flag[5] * flag[0] == 5658)
s.add(flag[10] + flag[32] + 228 == 441)
s.add(flag[35] * flag[0] == 1518)
s.add(flag[30] | flag[8] == 113)
s.add(flag[28] - flag[34] == 11)
s.add(flag[26] * flag[14] == 9975)
s.add(flag[31] * flag[22] == 10605)
s.add(flag[26] * flag[32] * 239 == 2452140)
s.add(flag[28] * flag[38] == 13875)
s.add(flag[18] + flag[16] == 190)
s.add(flag[27] + flag[26] + 96 == 290)
s.add(flag[22] - flag[38] == -24)
s.add(flag[33] + flag[5] == 224)
s.add(flag[19] * flag[16] == 10355)
s.add(flag[27] + flag[1] == 158)
s.add(flag[33] + flag[12] == 202)
s.add(flag[19] * flag[23] == 10355)

# Giải bài toán
if s.check() == sat:
    m = s.model()
    result = ''.join([chr(m[c].as_long()) for c in flag])
    print("✅ Flag tìm được là:", result)
else:
    print("❌ Không tìm được flag.")
