# yifinance

1. 價格與市場行情
- currentPrice：當下股價
- previousClose：昨收價。
- open：今日開盤價。
- dayHigh / dayLow：今日最高 / 最低價。
- fiftyTwoWeekHigh / fiftyTwoWeekLow：52週（近一年）最高 / 最低價。
- marketCap：總市值（單位為該股票的計價幣別，如台幣或美金）。
- volume：當日成交量。
- averageVolume：平均成交量（通常是近三個月的平均，用來判斷流動性）。
2. 公司基本資料 (Company Profile)
- shortName / longName：公司簡稱 / 全名。
- sector：所屬板塊 / 產業大類（如：Technology 科技業）。
- industry：所屬細分行業（如：Semiconductors 半導體）。
- country：公司所在國家。
- website：公司官方網站。
- longBusinessSummary：公司的長篇業務介紹（英文）。
3. 估值與獲利能力
- trailingPE：歷史本益比（P/E Ratio）。
- forwardPE：預估本益比。
- priceToBook：股價淨值比（P/B Ratio）。
- trailingEps：過去12個月的每股盈餘（EPS）。
- profitMargins：淨利率。
- operatingMargins：營業利益率。
- returnOnAssets (ROA)：資產報酬率。
- returnOnEquity (ROE)：股東權益報酬率。
4. 股息與風險指標
- dividendYield：殖利率（例如回傳 0.025 代表 2.5%）。
- dividendRate：預估每年配發的現金股利金額。
- beta：用來衡量股票波動度，大於 1 代表波動比大盤劇烈，小於 1 代表比大盤平穩。