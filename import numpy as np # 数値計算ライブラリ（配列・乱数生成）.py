import numpy as np                      # 数値計算ライブラリ（配列・乱数生成）
import pandas as pd                    # 表形式データを扱うライブラリ
from scipy.sparse import csr_matrix    # 疎行列（メモリ効率の良い行列）を使う
import anndata as ad                   # AnnDataオブジェクトのためのライブラリ

# 100細胞 × 2000遺伝子のランダムなカウントデータ（ポアソン分布に従う）
counts = csr_matrix(np.random.poisson(1, size=(100, 2000)), dtype=np.float32)

# そのデータを使って AnnData オブジェクトを作成
adata = ad.AnnData(X=counts)

# 結果表示
print(adata)

# 各細胞に「T細胞」「B細胞」いずれかをランダムに割り当てる
adata.obs["cell_type"] = np.random.choice(["T", "B"], size=adata.n_obs)

# 各遺伝子に名前を付ける（gene0, gene1, ..., gene1999）
adata.var["gene_symbols"] = [f"gene{i}" for i in range(adata.n_vars)]

# 確認してみよう
print(adata.obs.head())
print(adata.var.head())
