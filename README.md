# LMP LP「その街で、いちばん頼られる賃貸屋さんへ。」

賃貸仲介・管理会社向けのLMP加盟LP。
`https://lmp-rental-future.uminchu-t0422.chatgpt.site/` の複製版（編集可能な形に分解済み）。

## ファイル構成

| ファイル | 内容 |
|---|---|
| `index.html` | 本文。ここを直接編集する |
| `style.css` | 全スタイル（元は`<style>`インライン） |
| `script.js` | LINEボタンのフォールバック＋固定ボトムバーの表示制御 |

元サイトにあったCloudflareの計測スクリプトは削除済み。画像ファイルは使っていない。

## 元サイトからの変更点

- CSS・JSを外部ファイルに分離、改行を入れて編集できる形に整形
- 最終CTAをLINE導線に変更（`.line-card`）。元の「LMPの成長モデルをもう一度見る」はその下のテキストリンクとして残した
- 固定ボトムバー（`#cta-bar`）を追加。ヒーローを過ぎるとせり上がる
- ヘッダーロゴの空リンク `href="#"` をページ先頭 `#top` に変更

## 問い合わせ先

LINE公式アカウント（LMP共通）: https://lin.ee/vV1leDB

`index.html` 内に4か所（LINEカード2・固定バー2）。変更するときは一括置換する。

## セクション構成

`#issues` 賃貸経営の課題 → `#system` LMPの仕組み → `#future` 収益ルート → 想い → FAQ → クロージング

## プレビュー

`.claude/launch.json` に `lmp-rental-future-lp`（ポート8985）で登録済み。

## 公開

未公開。GitHub Pagesに出す場合は `lmp-next-era-lp` と同じ手順。
