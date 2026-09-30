FILE_name = "product.csv"

# Đọc dữ liệu từ file
def read_product():
    with open(FILE_name, "r") as file:
        # Bỏ qua dòng đầu
        file.readline()
        # Đọc tiếp từ dòng thứ 2
        for line in file:
            line = line.strip() # bỏ ký tự \n ở cuối mỗi dòng

            # cắt chuỗi thành mảng
            data = line.split(",")
            # Tạo sp theo dang dictionary
            propduct ={
                "id": data[0],
                "name": data[1],
                "price"
            }


read_product()

# Hàm hiển thị sản phẩm
def display_product():
    pass

# Hàm thêm sp
def add_product():
    pass

# Hàm tìm kiếm sản phẩm
def search_product():
    pass

# Hàm lưu sp
def save_product():
    pass


# Main Menu
def main():

    while True:
        print("******************Menu******************")
        print("1. Display all products")
        print("2. Add product")
        print("3. Search product by id")
        print("4. Save products to file")
        print("5. Exit program")
        print("******************Menu******************")

        choice = input("Enter your choice: ")
        if choice == "1":
            display_product()
        elif choice == "2":
            add_product()
        elif choice == "3":
            search_product()
        elif choice == "4":
            save_product()
        elif choice == "5":
            print("Exit program")
            break
        else: 
            print ("Wrong choice. Enter 1-5")

# gọi hàm main
main()




