soGioLam = float(input('Nhap so gio lam moi tuan: '))
luongGio = float(input('Nhap thu lao tren moi gio tieu chuan: '))
gioTieuChuan = 44
gioVuotChuan = max(0, soGioLam - gioTieuChuan)

thucLinh = gioTieuChuan * luongGio + gioVuotChuan * luongGio * 1.5

print('So tien thuc linh cua nhan vien:', thucLinh)
