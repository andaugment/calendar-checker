"""空き時間チェッカー 仕様書PDF生成スクリプト"""
from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT_PATH = "C:/Windows/Fonts/NotoSansJP-Regular.otf"
FONT_BOLD_PATH = "C:/Windows/Fonts/NotoSansJP-Bold.otf"
OUTPUT = "E:/Claude/projects/calendar-checker/空き時間チェッカー_仕様書.pdf"

APP_URL = "https://schedule-checker-848.netlify.app"
GITHUB_URL = "https://github.com/andaugment/calendar-checker"


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("NotoSans", "", FONT_PATH)
        self.add_font("NotoSans", "B", FONT_BOLD_PATH)
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("NotoSans", "", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, "空き時間チェッカー 仕様書", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("NotoSans", "", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"{self.page_no()}", align="C")
        self.set_text_color(0, 0, 0)

    def h1(self, text):
        self.set_font("NotoSans", "B", 20)
        self.set_text_color(0, 120, 212)
        self.ln(4)
        self.multi_cell(0, 10, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def h2(self, text):
        self.ln(6)
        self.set_font("NotoSans", "B", 14)
        self.set_fill_color(0, 120, 212)
        self.set_text_color(255, 255, 255)
        self.cell(0, 9, f"  {text}", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(0, 0, 0)
        self.ln(3)

    def h3(self, text):
        self.ln(4)
        self.set_font("NotoSans", "B", 11)
        self.set_text_color(0, 80, 160)
        self.multi_cell(0, 7, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def body(self, text):
        self.set_font("NotoSans", "", 10)
        self.multi_cell(0, 6, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def bullet(self, text, indent=5):
        self.set_font("NotoSans", "", 10)
        x = self.get_x()
        self.set_x(self.l_margin + indent)
        self.multi_cell(0, 6, f"• {text}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_x(x)

    def table_row(self, col1, col2, header=False, bg=None):
        self.set_font("NotoSans", "B" if header else "", 9)
        if header:
            self.set_fill_color(230, 240, 255)
        elif bg:
            self.set_fill_color(*bg)
        else:
            self.set_fill_color(255, 255, 255)
        w1, w2 = 55, 125
        h = 7
        x_start = self.l_margin
        y_start = self.get_y()

        # Col1
        self.set_xy(x_start, y_start)
        self.multi_cell(w1, h, col1, border=1, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
        h1 = self.get_y() - y_start

        # Col2
        self.set_xy(x_start + w1, y_start)
        self.multi_cell(w2, h, col2, border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.TOP)
        h2 = self.get_y() - y_start

        row_h = max(h1, h2)
        self.set_y(y_start + row_h)

    def label_value(self, label, value):
        self.set_font("NotoSans", "B", 10)
        self.cell(45, 7, label, new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font("NotoSans", "", 10)
        self.multi_cell(0, 7, value, new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def build():
    pdf = PDF()
    pdf.set_margins(20, 20, 20)

    # ─── 表紙 ───
    pdf.add_page()
    pdf.ln(30)
    pdf.set_font("NotoSans", "B", 28)
    pdf.set_text_color(0, 120, 212)
    pdf.cell(0, 14, "空き時間チェッカー", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("NotoSans", "B", 18)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(0, 10, "仕様書", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(10)

    pdf.set_draw_color(0, 120, 212)
    pdf.set_line_width(0.8)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(10)

    pdf.set_font("NotoSans", "", 11)
    pdf.set_text_color(0, 0, 0)
    pdf.label_value("アプリURL：", APP_URL)
    pdf.ln(1)
    pdf.label_value("GitHubリポジトリ：", GITHUB_URL)
    pdf.ln(1)
    pdf.label_value("作成日：", "2026年5月16日")
    pdf.ln(1)
    pdf.label_value("作成者：", "andaugment")

    pdf.ln(20)
    pdf.set_font("NotoSans", "", 10)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 7,
        "本ドキュメントは「空き時間チェッカー」の仕様をまとめたものです。\n"
        "AI初心者向け学習素材としての活用方法、および今後の開発者向け体制への"
        "移行方針についても記載しています。",
        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(0, 0, 0)

    # ─── 1. 概要 ───
    pdf.add_page()
    pdf.h2("1. 概要")
    pdf.body(
        "Outlookカレンダー（Microsoft 365）と連携し、指定した条件の空き時間を自動検索・"
        "表示するWebアプリです。空いているスロットをクリックするだけで、そのままOutlookに"
        "予定を追加できます。"
    )

    pdf.h3("アクセス情報")
    pdf.label_value("公開URL：", APP_URL)
    pdf.ln(2)
    pdf.label_value("リポジトリ：", GITHUB_URL)
    pdf.ln(2)
    pdf.label_value("ホスティング：", "Netlify（GitHub mainブランチへpushで自動デプロイ）")

    pdf.h3("主な用途")
    pdf.bullet("日程調整時に「いつ空いているか」をすぐ確認したい")
    pdf.bullet("空きスロットをそのまま予定化したい")
    pdf.bullet("土日祝・バッファ時間を考慮した正確な空き時間を把握したい")

    # ─── 2. 機能一覧 ───
    pdf.h2("2. 機能一覧")

    pdf.h3("2-1. 認証・ログイン")
    pdf.bullet("Azure AD（Microsoft Entra ID）によるOAuth2認証")
    pdf.bullet("個人・職場のMicrosoftアカウントに対応")
    pdf.bullet("前回ログインしたアカウントで自動ログイン")
    pdf.bullet("ログアウト機能あり")

    pdf.h3("2-2. 空き時間検索")
    pdf.bullet("Microsoft Graph APIでカレンダーイベントを取得")
    pdf.bullet("営業時間内での空きスロットを自動計算")
    pdf.bullet("日本の祝日を自動判定（2025〜2028年対応）")
    pdf.bullet("バッファ時間を考慮した正確なブロック計算")
    pdf.bullet("隣接する予定の情報（前後に何があるか）も表示")

    pdf.h3("2-3. 表示モード")
    pdf.bullet("リスト表示：日付単位でグループ化。時間帯・隣接イベント・所要時間を表示")
    pdf.bullet("カレンダー表示（週表示）：予定（濃紫）と空きスロット（緑）を時系列で重ねて表示")

    pdf.h3("2-4. 予定追加")
    pdf.bullet("空きスロットをクリックしてモーダルを開き、タイトル・時間・メモを入力")
    pdf.bullet("Microsoft Graph API（POST /me/events）でOutlookに直接保存")
    pdf.bullet("追加後は自動で検索結果をリフレッシュ")

    pdf.h3("2-5. その他")
    pdf.bullet("コピー機能：検索結果をテキスト形式でクリップボードにコピー")
    pdf.bullet("設定の永続化：検索条件をlocalStorageに保存し、次回訪問時に復元")
    pdf.bullet("トースト通知：成功・エラーを画面下部に3秒表示")

    # ─── 3. 検索条件パラメータ ───
    pdf.add_page()
    pdf.h2("3. 検索条件パラメータ")

    pdf.table_row("パラメータ", "内容・デフォルト値", header=True)
    rows = [
        ("開始日・終了日", "検索対象の日付範囲。デフォルト：今日〜翌週月曜+4日"),
        ("営業開始・終了時刻", "デフォルト：09:00〜18:00"),
        ("前後バッファ", "予定の前後に確保する時間。選択肢：0/15/30/45/60/90/120分（デフォルト：60分）"),
        ("必要最小空き時間", "表示する空きスロットの最小長さ。選択肢：15/30/45/60/90/120/180分（デフォルト：60分）"),
        ("土日祝を除外", "チェックボックス。デフォルト：有効（除外する）"),
    ]
    alt = [(245, 250, 255), (255, 255, 255)]
    for i, (k, v) in enumerate(rows):
        pdf.table_row(k, v, bg=alt[i % 2])

    # ─── 4. 技術構成 ───
    pdf.h2("4. 技術構成（現状）")

    pdf.h3("フロントエンド")
    pdf.table_row("要素", "内容", header=True)
    tech_rows = [
        ("言語", "JavaScript (ES6) + HTML + CSS"),
        ("フレームワーク", "なし（Vanilla JS）"),
        ("外部ライブラリ", "@azure/msal-browser@2（CDN経由）"),
        ("PWA", "Service Worker によるキャッシュ対応"),
        ("ファイル構成", "index.html に全コード集約（HTML・CSS・JS）"),
    ]
    for i, (k, v) in enumerate(tech_rows):
        pdf.table_row(k, v, bg=alt[i % 2])

    pdf.h3("API")
    pdf.table_row("エンドポイント", "用途", header=True)
    api_rows = [
        ("GET /v1.0/me/calendarView", "カレンダーイベント取得（最大200件）"),
        ("POST /v1.0/me/events", "新規予定の追加"),
        ("スコープ", "Calendars.Read, Calendars.ReadWrite"),
    ]
    for i, (k, v) in enumerate(api_rows):
        pdf.table_row(k, v, bg=alt[i % 2])

    pdf.h3("インフラ・デプロイ")
    pdf.table_row("要素", "内容", header=True)
    infra_rows = [
        ("ホスティング", "Netlify"),
        ("CI/CD", "GitHub Actions（mainブランチpushで自動デプロイ）"),
        ("ローカル開発", "start.bat → Python標準HTTPサーバー（ポート8080）"),
    ]
    for i, (k, v) in enumerate(infra_rows):
        pdf.table_row(k, v, bg=alt[i % 2])

    # ─── 5. ファイル構成 ───
    pdf.add_page()
    pdf.h2("5. ファイル構成")

    pdf.table_row("ファイル", "役割", header=True)
    file_rows = [
        ("index.html", "全UI・CSS・JavaScriptコード（単一ファイル）"),
        ("manifest.json", "PWAマニフェスト（アプリ名・アイコン・テーマ色）"),
        ("sw.js", "Service Worker（キャッシング戦略）"),
        ("icon.svg", "PWA・ブラウザアイコン"),
        ("_headers", "Netlifyセキュリティヘッダー設定（CSP等）"),
        (".github/workflows/deploy.yml", "GitHub Actionsデプロイフロー"),
        ("start.bat", "ローカル開発サーバー起動スクリプト"),
        ("patch_all.py / patch.py", "コードパッチ適用スクリプト（補助用）"),
    ]
    for i, (k, v) in enumerate(file_rows):
        pdf.table_row(k, v, bg=alt[i % 2])

    # ─── 6. AI初心者向け練習ガイド ───
    pdf.h2("6. AI初心者向け練習ガイド")
    pdf.body(
        "このアプリをベースに、AIコーディング（Cursor等）の練習を段階的に進められます。"
    )

    steps = [
        ("Step 1：動かして確認する",
         "start.batでローカルサーバーを起動し、ブラウザで動作確認する。\nMicrosoftアカウントでログインして空き時間を検索してみる。"),
        ("Step 2：UI変更を依頼する",
         "AIに「ボタンの色を変えて」「タイトルを変えて」などを依頼する。\n最小限の変更で達成感を得られる。"),
        ("Step 3：機能追加を依頼する",
         "例：「検索結果を曜日でフィルタリングしたい」\n例：「コピーするテキストのフォーマットを変えたい」"),
        ("Step 4：バグを直す",
         "意図的にバグを仕込んだブランチを渡して、AIと一緒に原因を特定・修正する練習をする。"),
    ]

    for title, desc in steps:
        pdf.h3(title)
        pdf.body(desc)

    # ─── 7. 今後の開発者向け体制 ───
    pdf.add_page()
    pdf.h2("7. 今後の開発者向け体制への移行方針")

    pdf.h3("現状の課題")
    pdf.body(
        "index.html 1ファイルにHTML・CSS・JavaScriptが全て集約されており、"
        "実際の開発者にとって読みにくく、差分レビューや分担作業がしにくい構造になっています。"
    )

    pdf.h3("推奨ファイル分割構成")
    pdf.set_font("NotoSans", "", 10)
    pdf.set_fill_color(245, 245, 245)
    code = (
        "src/\n"
        "  auth.js          # 認証ロジック（Azure AD / MSAL）\n"
        "  calendar.js      # カレンダーAPI呼び出し・空き時間計算\n"
        "  ui.js            # DOM操作・表示ロジック\n"
        "  holidays.js      # 祝日データ\n"
        "  index.html       # HTMLのみ\n"
        "  style.css        # CSSのみ"
    )
    pdf.multi_cell(0, 6, code, border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

    pdf.h3("言語・スタック選択の方針")
    pdf.table_row("選択肢", "向いている場面", header=True)
    stack_rows = [
        ("Vanilla JS（現状）", "AI初心者の練習用。ビルド不要・即確認できる"),
        ("TypeScript + Vite", "実際の開発者が入るフェーズ。型安全・補完が効く"),
        ("React + TypeScript", "チームで分担開発するフェーズ。コンポーネント分割しやすい"),
    ]
    for i, (k, v) in enumerate(stack_rows):
        pdf.table_row(k, v, bg=alt[i % 2])

    pdf.ln(4)
    pdf.h3("移行ロードマップ（案）")
    pdf.bullet("Phase 1（現在）：Vanilla JS のまま。AI初心者に練習させる")
    pdf.bullet("Phase 2：ファイル分割のみ実施（TypeScriptなし・ビルドなし）")
    pdf.bullet("Phase 3：TypeScript + Vite 化。開発者が修正しやすい体制へ")
    pdf.bullet("Phase 4（任意）：React 化。チーム開発・コンポーネント再利用へ")

    pdf.output(OUTPUT)
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    build()
