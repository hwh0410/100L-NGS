# 100L NGS — 百公升厭氧槽菌相研究

以高氮食品污泥與檸檬酸酸洗椰殼活性碳進料之穩定期出料樣本，整理 16S 菌相資料與生物學判讀。

- [互動分析頁](https://hwh0410.github.io/100L-NGS/)
- [完整研究分析](ANALYSIS.md)
- [完整 ASV 資料](data/asv.csv)
- [核對紀錄及來源檔案雜湊](data/audit.json)

## 分析範圍

樣本 `An-100L-0929`，16S V3–V4，DADA2，SILVA 138.2。62,557 有效 reads、521 ASV；單一樣本，沒有處理對照與生物重複。古菌共 2,108 reads；Methanosarcina 為 1,603 reads，占本次檢出古菌 76.04%。

頁面支援菌門／菌科／菌屬圖表、古菌占比分母切換、七階層分類搜尋、分類域與占比篩選、排序、CSV 匯出及列印完整分析。沒有外部前端套件、登入、追蹤器或資料上傳。所有前端資料皆為本次固定樣本。

讀數為擴增後序列數，並非菌體絕對數。功能為文獻推論，不能把菌相快照當成 SAO、DIET、耐氨或酸洗效益的實測證據。完整 PICRUSt2／Tax4Fun2／FAPROTAX 輸出並未隨附件提供，因此未建立功能排名。

## 資料來源與重現

原始來源為使用者上傳 `NT261008008_Report3.zip`，包含 `report/FullTable_abs_abun.xlsx`、`report/FullTable_rel_abun.xlsx` 及 HTML 報告。此 repo 保存衍生 CSV、摘要 JSON、完整判讀與程式，不重新發布定序公司的原始報告或圖像。工作表維度誤標 A1，讀取時重置維度並核對實際列，未改寫原檔。

有來源檔案及 Python/openpyxl 時，可重新擷取：

```bash
python scripts/extract.py /path/to/report --output data
python scripts/build.py
python scripts/verify.py
node --check app.js
```

`extract.py` 逐階層核對 reads，逐筆比較相對／絕對豐度並重算多樣性，輸出來源 SHA-256。`build.py` 將 `ANALYSIS.md` 插入 `index.template.html`，產生可直接部署的 `index.html`。修改分析文字後應重新執行 build。

`data/*.csv` 為原始豐度表各階層加上 `percent_total` 的衍生資料，ASV 表保留代表序列。`community.json` 及 `data.js` 的階層摘要由 ASV 表重新彙整，包含 reads 與 ASV 數；每一階層 reads 加總為 62,557。`UNCLASSIFIED`／`Incertae_Sedis` 尾碼保留報告區分譜系的標記，不能跨譜系隨意合併。

本次未取得原始 FASTQ，故無法重跑定序 QC。引用文獻及各項限制見完整分析。

## 部署

建置輸出已提交至根目錄。GitHub Pages 使用 `main` 分支的 `/ (root)`，`.nojekyll` 停用 Jekyll 處理。無需安裝或提供 API 金鑰。亦可使用任意靜態網頁伺服器開啟。
