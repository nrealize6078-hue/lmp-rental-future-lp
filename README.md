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
- スマホ対応を補強（下記）

## スマホ対応

元サイトのブレークポイントは `@media(max-width:800px)` の**1段階だけ**で、
375pxでも課題セクション（`.pain-grid`）が2列のまま、カード幅164pxに19pxの見出しが入り、
`<br>` で整えた改行がさらに語中で折り返されていた。

`@media(max-width:560px)` を追加して対処。

| 対象 | 内容 |
|---|---|
| `.pain-grid` / `.flow` | 1列にする |
| `h2` | `clamp(23px,7.2vw,29px)` |
| `.pivot h2` / `.closing h2` | `clamp(25px,8.1vw,31px)` |
| `.solution h3` | `clamp(19px,5.5vw,23px)` |

**560pxを超える表示（パソコン・タブレット）は一切変わらない。**

検証済み: 375px・320pxとも横スクロールなし、はみ出し要素0件。
新しくセクションを足すときは、375pxと320pxの両方で見出しの折り返しを確認すること。

## 問い合わせ先

LINE公式アカウント（LMP共通）: https://lin.ee/vV1leDB

`index.html` 内に4か所（LINEカード2・固定バー2）。変更するときは一括置換する。

## セクション構成

`#issues` 賃貸経営の課題 → `#system` LMPの仕組み → `#future` 収益ルート → 想い → FAQ → クロージング

## プレビュー

`.claude/launch.json` に `lmp-rental-future-lp`（ポート8985）で登録済み。

## 公開

- 公開URL: https://nrealize6078-hue.github.io/lmp-rental-future-lp/
- リポジトリ: https://github.com/nrealize6078-hue/lmp-rental-future-lp （public）
- GitHub Pages（main / ルート）。**検索エンジンに掲載する設定**（noindexは入れていない）

更新するときは、このフォルダで編集して commit → push すれば1〜2分で反映される。

```bash
git add -A && git commit -m "内容を修正" && git push
```
