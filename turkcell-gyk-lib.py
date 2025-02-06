"""
2. ödev
Kütüphane Yönetim Sistemi (Encapsulation, Composition, Exception Handling)
Bu projede bir kütüphane sistemini modelleyeceğiz.
Şartlar:
Kitap sınıfı:
Kitap adı, yazar, sayfa sayısı, ISBN bilgilerini içermeli.

Kutuphane sınıfı:
Kitap ekleme (kitap_ekle(kitap)), kitap kaldırma (kitap_sil(isbn)), tüm kitapları gösterme (kitaplari_goster()) metodları olmalı.
Exception Handling (Hata Yakalama): Bir kitap zaten ekliyse hata fırlatmalı.

BENSU ÖZTÜRK - FATMA SENA YÜKSEL
"""
class Book:
    def __init__(self, name, author, page, isbn):
        self._name = name
        self._author = author
        self._page = page
        self._isbn = isbn
        print(f"Kitap oluşturuldu.")

    def get_isbn(self):
        return self._isbn
    def get_page(self):
        return self._page
    def get_name(self):
        return self._name
    def get_author(self):
        return self._author

class Lib:
    def __init__(self):
        self.book_list = {}

    def add(self):
        try:
            while True:
                book_name = input("Eklemek istediğiniz kitap ismini giriniz: ").strip()
                author = input("Yazar ismini giriniz: ").strip()
                if book_name != "" and author != "":
                    if book_name in [book.get_name() and book.get_author for book in self.book_list.values()]:
                        raise ValueError(f"{book_name} Bu kitap mevcut")
                    else:
                        break
                else:
                    print("Girilen değerleri kontrol ediniz. Kitap adı ve yazar adı boş geçilemez.")
                    continue
                

            while True:
                page = input("Sayfa sayısını giriniz: ").strip()
                if page.isdigit():  
                    break
                else:
                    print("Hata: Lütfen geçerli bir sayfa sayısı giriniz. (Sadece rakamlar 0-9)")

            while True:
                isbn = input("Beş basamaklı ISBN numarasını giriniz: ").strip()
                
                if not (isbn.isdigit() and len(isbn) == 5):
                    print("Hatalı ISBN değeri! Lütfen beş basamaklı bir ISBN giriniz.")
                    continue 
                
                if isbn in self.book_list:
                    print(f"Hata: Bu ISBN değeri başka bir kitap adına kayıtlı! Lütfen doğru ISBN değerini giriniz.")
                    continue 
                
                break

            new_book = Book(book_name, author, page, isbn)
            self.book_list[new_book.get_isbn()] = new_book
            print(f"\n{'='*40}")
            print(f"{'Kitap Adı:':<20} {new_book.get_name()}")
            print(f"{'Yazar:':<20} {new_book.get_author()}")
            print(f"{'Sayfa Sayısı:':<20} {new_book.get_page()}")
            print(f"{'ISBN:':<20} {new_book.get_isbn()}")
            print(f"\n{'='*40}")
            print(f"{new_book.get_name()} kütüphaneye başarıyla eklendi!\n")


        except ValueError as e:
            print(f"Hata: {e}")

        except Exception as ex:
            print(f"Beklenmeyen bir hata oluştu: {ex}")

    def delete(self):
        try:
            book_isbn_deleted = input("Silmek istediğiniz kitabin ISBN değerini giriniz: ").strip()
            if not book_isbn_deleted.isdigit() or len(book_isbn_deleted) != 5:
                    raise ValueError("ISBN sadece rakamlardan oluşmalıdır ve beş basamaklı olmalıdır.!")

            if book_isbn_deleted in self.book_list:
                
                print(f"{'\n Silinen Kitap Bilgileri:':^40}")
                deleted_book = self.book_list.pop(book_isbn_deleted)
                print(f"{'='*40}")
                print(f"{'Kitap Adı:':<15} {deleted_book.get_name():<25}")
                print(f"{'Yazar:':<15} {deleted_book.get_author():<25}")
                print(f"{'Sayfa Sayısı:':<15} {deleted_book.get_page():<25}")
                print(f"{'ISBN:':<15} {deleted_book.get_isbn():<25}")
                print(f"{'='*40}\n")


            else:
                print("Girilen ISBN değerine sahip kitap bulunamadı.")

        except ValueError as e:
            print(e)

        except Exception as ex:
            print(f"Beklenmeyen bir hata oluştu: {ex}")

    def show(self):
        print(f"{'Güncel Kitap Listesi:':^40}")
        if len(self.book_list) == 0:
            print(f"{'='*40}\n")
            print("Kütüphanede kitap bulunmamaktadır!")
        else:
            for book in self.book_list.values():
                print(f"{'='*40}\n")
                print(f"{'Kitap:':<20} {book.get_name()}")
                print(f"{'Yazar:':<20} {book.get_author()}")
                print(f"{'Sayfa:':<20} {book.get_page()}")
                print(f"{'ISBN:':<20} {book.get_isbn()}")



library = Lib()

library.show()
library.add()
library.add()
library.show()
print(" ")
library.delete()
print(" ")
library.show()