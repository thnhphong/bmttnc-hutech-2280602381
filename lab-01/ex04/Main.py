from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("Quan Ly Sinh Vien:");
    print("*-----------------------*");
    print("1. Them sinh vien");
    print("2. Cap nhat thong tin sinh vien theo ID");
    print("3. Xoa sinh vien theo ID");
    print("4. Tim kiem sinh vien theo ten");
    print("5. Sap xep sinh vien theo diem TB");
    print("6. Sap xep sinh vien theo ten");
    print("7. Hien thi danh sach sinh vien");
    print("0. Thoat");
    print("*-----------------------*");
    
    key = int(input("Nhap lua chon cua ban: "));
    if (key == 1):
        print("\nThem sinh vien:");
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien theo ID:")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien.")
            print("\nNhap ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh vien co id = ", ID, " da bi xoa.")
            else: 
                print("\nSinh vien co id = ", ID, " khong ton tai")
            
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else: 
            print("\nDanh sach sinh vien trong!")
    
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("5. Sap xep sinh vien theo diem TB");
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else: 
            print("\nDanh sach sinh vien trong!")
    
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("6. Sap xep sinh vien theo ten")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else: 
            print("\nDanh sach sinh vien trong!")
            
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("7. Hien thi danh sach sinh vien");
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else: 
            print("\nDanh sach sinh vien trong!")
    else: 
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong menu")
        