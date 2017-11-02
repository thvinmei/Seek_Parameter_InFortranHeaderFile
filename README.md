# Seek_Parameter_InFortranHeaderFile
Fortran用のヘッダファイル(.h)の中を検索し，指定した変数の定義値を抽出します．

## 使い方 (How To Use)
例えば下記のようなヘッダファイル(sample.h)に対して，
``` fortran
! -*- F90 -*-
    real,parameter :: realnumA=10.0
    integer,parameter :: intnumB=1
    logical,parameter :: logicC=.false.
```

コマンドラインで
``` bash
> python3 seek_in_fortran_header.py realnumA sample.h
10

> python3 seek_in_fortran_header.py intnumB sample.h
1

> python3 seek_in_fortran_header.py logicC sample.h
False
```
というように使えます．

---
## 注意
- 引数の個数チェックはしていません．
- 現時点のバージョンでは，変数名の部分一致でも検索結果が返ってきます．
- 検索に合致する変数が定義されていない場合，pythonのエラーが返ってきます．