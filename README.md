🔐 IoT Sensor Data Encryption using S-DES

📌 Aim

To simulate an IoT sensor sending data securely by encrypting it using the Simplified Data Encryption Standard (S-DES) algorithm and decrypting it at the cloud receiver.

---

📖 Description

This project demonstrates a basic IoT communication model where:

- A sensor device generates data (e.g., temperature readings)
- The data is encrypted using S-DES
- Encrypted data is transmitted over a network (socket)
- A cloud receiver decrypts and displays the original data

This simulation helps understand:

- Lightweight cryptography in IoT
- Secure data transmission
- Client-server communication using sockets

---

⚙️ Technologies Used

- Python 3
- Socket Programming
- Simplified DES (S-DES)

---

🧠 Theory

What is S-DES?

Simplified Data Encryption Standard (S-DES) is a lightweight version of the DES algorithm used for educational purposes. It operates on:

- 8-bit plaintext
- 10-bit key
- Produces 8-bit ciphertext

Why S-DES in IoT?

IoT devices often have:

- Limited processing power
- Low memory

So lightweight encryption like S-DES helps simulate secure communication without heavy computation.

---

🔄 System Architecture

IoT Sensor (Client)
        ↓
Encrypt Data (S-DES)
        ↓
Send via Socket
        ↓
Cloud Receiver (Server)
        ↓
Decrypt Data (S-DES)
        ↓
Display Original Data

---

🧾 Algorithm

🔑 Key Generation

1. Take a 10-bit key
2. Apply permutation (P10)
3. Split into two halves
4. Perform left shifts
5. Apply permutation (P8)
6. Generate two subkeys: K1 and K2

---

🔐 Encryption Process

1. Take 8-bit plaintext
2. Apply initial permutation (IP)
3. Split into left and right halves
4. Apply function fk using subkey K1
5. Swap halves
6. Apply function fk using subkey K2
7. Apply inverse permutation (IP⁻¹)
8. Output ciphertext

---

🔓 Decryption Process

1. Same as encryption
2. Use subkeys in reverse order (K2 then K1)

---

📁 Project Structure

iot-sdes-simulation/
│── sensor.py        # IoT device (client)
│── cloud.py         # Cloud receiver (server)
│── sdes.py          # S-DES algorithm implementation
│── requirements.txt
│── README.md

---

🚀 How to Run

✅ Step 1: Clone Repository

git clone https://github.com/your-username/iot-sdes-simulation.git
cd iot-sdes-simulation

---

✅ Step 2: Start Cloud Receiver

python cloud.py

---

✅ Step 3: Run Sensor

Open another terminal and run:

python sensor.py

---

📊 Sample Output

🖥️ Cloud Terminal

Cloud is waiting for data...
Connected by ('127.0.0.1', 54321)
Encrypted Received: 10101010
Decrypted Data: 10101010

---

📡 Sensor Terminal

Sensor Data: 10101010
Encrypted Data: 10101010

---

🔍 Explanation

- The sensor encrypts data before sending
- The cloud receives encrypted data
- Decryption restores the original sensor value
- Demonstrates secure communication in IoT

---

⚠️ Limitations

- This is a simplified implementation of S-DES
- Not suitable for real-world security
- No authentication or integrity checks

---

🌟 Future Enhancements

- Implement full S-DES with S-boxes
- Add AES for real-world security comparison
- Add GUI dashboard
- Use MQTT instead of sockets
- Deploy on real IoT hardware (Raspberry Pi / ESP32)

---

📚 Applications

- Smart homes
- Healthcare monitoring
- Industrial IoT
- Secure sensor networks

---

👨‍💻 Author

Heritharaan A

---

📜 License

This project is for educational purposes only.
