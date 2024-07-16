## 概要
ECサイトのイメージ。顧客と管理者用の機能を提供。

## データ
### 顧客マスタ

id

名前

年齢

### 商品マスタ

id

商品名

カテゴリ

説明

### 購入

id

顧客id

商品id

購入日

## 機能
### 顧客

商品閲覧（カテゴリでフィルター）

購入（一回につき１品１個まで）

購入履歴閲覧（購入日でフィルター）

### 管理者

商品登録

顧客登録

## API仕様
### 顧客

商品閲覧

・GET

・/customer/items/

・クエリパラメータ

・category: str | None

購入

・POST

・/customer/purchase/

・クエリパラメータ

  ・customer_id: int

  ・order_date_from: int | None

  ・category: str | None

購入履歴閲覧

・GET

・/customer/purchase/

### 管理者

商品登録

・POST

・/admin/item/

・リクエストボディ


顧客登録

・POST

・/admin/customer

・リクエストボディ


## 環境
ローカル

SQLite

 

 

 

 

 
