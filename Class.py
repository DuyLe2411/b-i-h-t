class Contact:
    def __init__(self,name='',phones=[],emails=[],address='',notes='',tags=[]):
        self.name = name
        self.phones = phones
        self.emails = emails
        self.address = address
        self.notes = notes
        self.tags = tags

    def set_name(self):
        name = input("Nhập tên:" )
        if name.isalpha():
            self.name = name
        else:
            print("Nhập tên không nhập số")
    def set_phones(self):
        phones =input("Nhập số điện thoại: ").split(",")
        if phones.isdigit():
            self.phones = phones
        else:
            print("Nhập SỐ ĐIỆN THOẠI")
    def set_emails(self):
        emails = input("Nhập emails: ").split(",")
        self.emails = emails
    def set_address(self):
        address = input("Nhập địa chỉ: ")
        self.address = address
    def set_notes(self):
        notes = input("Nhập ghi chú: ")
        self.notes = notes
    def set_tags(self):
        tags = input("Nhập tags: ").split(",")
        self.tags = tags
    
    def check_tag(self):
        tag = input("Nhập tag bạn muốn tìm: ").lower()
        for tag in self.tags:
            print(True)
            break
    def __str__(self) :
        return f"{self.name:<20}\t| {self.phones}\t| {self.emails}\t|  {self.address:<10}\t |  {self.notes:<20} |  {self.tags}"

    def is_friend(self,tag= "bạn bè"):
        return tag in self.tags

    def is_student(self,tag= "học viên"):
        return tag in  self.tags
    
    def is_enemy(self,tag="kẻ thù"):
        return tag in self.tags
    
    def is_junior(self,tag="đệ tử"):
        return tag in self.tags