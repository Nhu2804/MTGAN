import pandas as pd
import os

file_path = r"G:\Study\Paper\MTGAN-main\data\mimic3\raw\D_ICD_PROCEDURES.csv"
proc = pd.read_csv(file_path)

# Chuyển tên cột sang chữ thường để thống nhất
proc.columns = proc.columns.str.lower()

# Kiểm tra tên cột
print(proc.columns)

# Lấy đủ 3 cột: mã, mô tả ngắn, mô tả dài
map_proc = proc[['icd9_code', 'short_title', 'long_title']].rename(
    columns={
        'icd9_code': 'PROCEDURE CODE',
        'short_title': 'SHORT DESCRIPTION',
        'long_title': 'LONG DESCRIPTION'
    }
)

# Chuẩn hóa mã: bỏ dấu chấm để giống map.xlsx
map_proc['PROCEDURE CODE'] = map_proc['PROCEDURE CODE'].astype(str).str.replace('.', '', regex=False)

# Loại trùng và sắp xếp
map_proc = map_proc.drop_duplicates().sort_values(by='PROCEDURE CODE')

# Ghi ra file Excel
output_path = os.path.join(os.path.dirname(file_path), 'map_procedure.xlsx')
map_proc.to_excel(output_path, index=False)

print(f"✅ Đã tạo file: {output_path}")
