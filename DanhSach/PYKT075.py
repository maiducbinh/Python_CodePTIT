class SDT:
    def __init__(self, ngay, hoten, sdt):
        self.ngay = ngay
        self.hoten = hoten
        self.sdt = sdt
        self.ten = hoten.split(" ")[-1]
        self.ho = hoten.split(" ")[0:-1]
        self.ho = " ".join(self.ho)
    def __str__(self):
        return f"{self.hoten}: {self.sdt} {self.ngay}"

op = open("SOTAY.txt", "r")
ip = op.read().split("\n")
a = []
while len(ip) > 0:
    x = ip[0]
    ip.pop(0)
    if x[:4] == "Ngay":
        ngay = x[5:]
    elif len(ip) > 0:
        sdt = ip[0]
        ip.pop(0)
        a.append(SDT(ngay, x, sdt))
a.sort(key=lambda x: (x.ten, x.ho))
op.close()
op = open("DIENTHOAI.txt", "w")
for i in a:
    op.write(str(i) + "\n")
op.close()