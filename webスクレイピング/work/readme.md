
h1. 解析準備：urlを指定してhtmlファイルをダウンロードする
* convert_url2html.py --file [url一覧が入ったテキストファイル（default：url_list.txt）]
 * url_list.txtに記載されたURLをHTMLへ保存していく

h1. とりあえずデータを集める：DBにどう保存するか検討用
* 指定したフォルダ以下にあるhtmlを解析して任意のデータをcsv形式で収集する
 * ディレクトリはコードべた書きの相対パス
 * 収集するデータは適宜コードを修正する

h1. 解析用データ保存：htmlを読み込んでsqliteへ保存する
* store_races.py --dir [htmlを保存したフォルダ（default：data）]
 * htmlを読み込んでデータベースへ保存

h1. 当日のURLを取得する
* collectUrl.pyを実行して当日のurl一覧を取得する
* ★を実行して期待値を解析する

h1. URLから情報を取得し解析する
* ★どんな解析をするかは要検討
