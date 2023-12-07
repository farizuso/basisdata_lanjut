import tkinter as tk
import redis

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")

        # Inisialisasi Redis
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.counter_key = 'my_counter'

        # Buat label untuk menampilkan nilai counter
        self.counter_label = tk.Label(root, text="Counter Value: 0", font=("Helvetica", 16))
        self.counter_label.pack(pady=20)

        # Buat tombol untuk increment counter
        self.increment_button = tk.Button(root, text="Increment", command=self.increment_counter)
        self.increment_button.pack(pady=10)

        # Buat tombol untuk reset counter
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_counter)
        self.reset_button.pack(pady=10)

        # Perbarui nilai awal counter
        self.update_counter_value()

    def increment_counter(self):
        # Increment counter di Redis
        self.redis_client.incr(self.counter_key)
        # Perbarui nilai di antarmuka pengguna
        self.update_counter_value()


    def reset_counter(self):
        # Reset counter di Redis
        self.redis_client.set(self.counter_key, 0)
        # Perbarui nilai di antarmuka pengguna
        self.update_counter_value()

    def update_counter_value(self):
        # Dapatkan nilai counter dari Redis
        counter_value = self.redis_client.get(self.counter_key)
        # Perbarui label di antarmuka pengguna
        self.counter_label.config(text=f"Counter Value: {counter_value.decode('utf-8')}")


if __name__ == "__main__":
    # Buat jendela Tkinter
    root = tk.Tk()
    # Inisialisasi aplikasi
    app = CounterApp(root)
    # Jalankan aplikasi
    root.mainloop()
