import binascii
f = open("Φυσική.docx", "rb") #άνοιγμα αρχείου διαβάζοντας τα byte του 
def printL(L):
    y = ''
    count = 0
    for i in L:
        y = y + str(i) + ' '
        count += 1                      #εκτύπωση χαρακτήρων με κενό ανάμεσά τους και σε συγκεκριμένο αριθμό στηλών
        if count%16==0:y = y + '\n'
    if y[-1] != '\n': y = y + '\n'
    print(y)
def printl(l): 
    z = ''
    count = 0
    for o in l:
        z = z + str(o) + ''             #εκτύπωση χαρακτήρων σε συγκεκριμένο αριθμό στηλών
        count += 1
        if count%16==0:z = z + '\n'
    if z[-1] != '\n': z = z + '\n'
    print(z)
        

byte = f.read(1)
L=[]
l=[]
while byte:
    x = binascii.b2a_hex(byte) #μετατροπή bytes σε δεκαεξαδικούς χαρακτήρες του ascii
    a = str(x) 
    b = a.upper()           #μετατροπή των χαρακτήρων σε string, κεφαλαιοποίηση  των 'γραμμάτων' και ταξινόμηση τους σε λίστα
    L.append(b[2:4])
    c = str(byte)
    if len(c)> 4:
        g = c[4:6]
        if g.startswith('0') or g.startswith('1'):      #μετατροπή των byte σε string, τύπωσή τους ανάλογα με το μήκος της 'λέξης' που τα περιγράφει και ταξινόμηση τους σε λίστα
            g = '.'
        elif g == 'a0' or g == '20':
            g = ' '
        l.append(g)
    else:
        h = c[2:3]
        l.append(h)
        
    byte = f.read(1)
printL(L)
printl(l)
f.close()
