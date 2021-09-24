from Class import Contact
quoc_duy = Contact(name="Lê Quốc Duy",
                    phones=[8448004717],
                    emails=['duyzuize@gmail.com','lequocduy2411@gmail.com'],
                    address="K110/33 Phan Thanh",
                    notes="Vui tính",
                    tags=["bạn bè","học viên"])

minh_triet = Contact(name="Nguyễn Minh Triết",
                    phones=[8448004717],
                    emails=['trietzuize@gmail.com','lequocduy2411@gmail.com'],
                    address="K110/33 Hoàng Diệu",
                    notes="Vui tính, Óc chó",
                    tags=["bạn bè","học viên","đệ tử"])
hoang_khai = Contact(name="Nguyễn Hoàng Khải",
                    phones=[8448004717],
                    emails=['khaizuize@gmail.com','lequocduy2411@gmail.com'],
                    address="K110/33 Hải Phòng",
                    notes="Thằng đần",
                    tags=["kẻ thù","học viên","đệ tử"])
contact_list = [quoc_duy,minh_triet,hoang_khai]
tag = input("Nhập tag bạn muốn tìm: ")

for contact in contact_list:

    if contact.is_friend(tag):
        print(contact)
    elif contact.is_enemy(tag):
        print(contact)
    elif contact.is_junior(tag):
        print(contact)
    elif contact.is_student(tag):
        print(contact)