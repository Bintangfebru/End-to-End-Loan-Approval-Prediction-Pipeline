from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model_credit (2).pkl")

@app.route('/')
def home():
    return render_template('index.html', prediction=None, form_data=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Simpan nilai string dulu untuk dikirim balik ke template
    form_data = {
        "rasio_pinjaman_terhadap_pendapatan": request.form['rasio_pinjaman_terhadap_pendapatan'],
        "gagal_bayar_tercatat":               request.form['gagal_bayar_tercatat'],
        "tunggakan_2thn_terakhir":            request.form['tunggakan_2thn_terakhir'],
        "skor_kredit":                        request.form['skor_kredit'],
        "usia":                               request.form['usia'],
        "lama_riwayat_kredit_tahun":          request.form['lama_riwayat_kredit_tahun'],
    }

    # Konversi ke float untuk model
    data = {k: float(v) for k, v in form_data.items()}

    df = pd.DataFrame([data])
    pred = model.predict(df)[0]

    if pred == 1:
        result = "Approved ✅"
    else:
        result = "Rejected ❌"

    # Kirim form_data (string) kembali ke template agar input tidak kosong
    return render_template('index.html', prediction=result, form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)