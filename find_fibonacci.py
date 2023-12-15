def rumus_fibonacci(x):
    # Inisialisasi dua angka pertama dalam deret Fibonacci
    a, b = 0, 1

    # Lakukan iterasi sampai nilai b lebih besar atau sama dengan x
    while b < x:
        # Update nilai a dan b sesuai aturan deret Fibonacci
        a, b = b, a + b

    # Cek apakah x sama dengan nilai terakhir b, jika iya, x termasuk dalam deret Fibonacci
    return b == x

def find_fibonacci(x):

  hasil = rumus_fibonacci(x)

  if hasil:
      print(x,"Termasuk dalam deret Fibonacci")
  else:
      print(x, "Tidak termasuk dalam deret Fibonacci")


if __name__ == "__main__":
    """Jalankan beberapa test-case di bawah sini
    """
    print(find_fibonacci(1))
    print(find_fibonacci(10))
    print(find_fibonacci(11))