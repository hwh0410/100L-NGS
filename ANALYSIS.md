# 百公升厭氧槽菌相分析

樣本 An-100L-0929。分析版本：2026-11-06。資料來源：NT261008008_Report3.zip 中的 FullTable_abs_abun.xlsx、FullTable_rel_abun.xlsx 及 HTML 報告。這是一份穩定操作時的單點菌相快照，並非處理前後比較。

## 1. 核心判讀

本樣本可見發酵細菌、脂肪酸共營養代謝相關菌，以及多種產甲烷古菌。Methanosarcina 在本次檢出的古菌序列中占優勢，支持將其列為後續追蹤的重點產甲烷菌屬。菌相與使用者描述的穩定產沼氣狀態相容，但單一時間點的 DNA 資料，不能證明哪一菌屬實際貢獻最多甲烷。

最值得研究的兩個方向是：Methanosarcina 可能參與的多種產甲烷途徑，以及高比例但分類未明的 Cloacimonadota 在中間酸轉換中的角色。現有資料尚不足以認定系統已由乙酸裂解轉成共營養乙酸氧化（SAO），也不足以認定活性碳已促進直接種間電子傳遞（DIET）。

## 2. 操作背景與資料邊界

| 項目 | 已知條件／待釐清事項 |
| --- | --- |
| 反應器 | 實驗室百公升厭氧槽；有效容積、混合與進出料方式未提供 |
| 原料 | 高氮含量食品污泥；目前未提供 TKN、TAN 或蛋白質含量 |
| 馴養 | 由低負荷逐漸增加；缺少負荷與採樣時間序列 |
| 進料 TS | 約 15%；需確認是加碳前污泥或加碳後混合物 |
| 停留時間 | 28 天；需確認是水力停留時間或批次操作週期，不能直接視為 SRT |
| 活性碳 | 粉末狀椰殼活性碳，先經檸檬酸酸洗；添加量為總進料 5%，重量基準待確認 |
| 產氣表現 | 使用者提供 650–700 L-biogas/kg-VS；未附連續紀錄、甲烷比例、氣體標準化條件及 VS 分母定義 |
| 溫度與化學監測 | 本次未提供溫度、pH、TAN、VFA、鹼度與硫化物 |
| 生物樣本 | 僅 1 件出料沼渣；沒有進料、接種源、未加碳對照或生物重複 |

以上操作數據是使用者提供的背景，並非 NGS 報告量測。樣本名稱中的 0929 不足以確認採樣年份或當日操作條件。

## 3. 定序品質與分類可靠度

使用 16S rRNA 基因 V3–V4 擴增子定序、DADA2 去雜訊及 SILVA 138.2 分類，並非 shotgun 宏基因體定序。DADA2 輸入 72,114 read pairs，非嵌合體且通過分類過濾者為 62,557，保留率為 86.75%。原報告的 retained_percent=100% 指「分類過濾這一步」保留率，不能解讀為全流程保留率。

共 521 個 ASV。依原始 reads 重算，Shannon（log2）為 6.6074、Gini–Simpson 為 0.97357、偏差校正 Chao1 為 521.2308，與原報告相符。報告顯示稀釋曲線趨於飽和，可支持已涵蓋本方法可檢出的主要多樣性；不能排除引子漏失族群，亦不能證明採樣具有時間代表性。DADA2 不推斷只受單一 read 支持的 ASV，因此 Chao1 接近 observed ASVs 也需配合此過濾條件解讀。

本次 7 個分類階層的序列加總都等於 62,557，絕對與相對豐度表逐筆一致（浮點誤差小於 10⁻¹⁰）。ASV 表另有可供重新分類的代表序列，但附件沒有原始 FASTQ，無法從原始定序訊號重跑品質控制。

報告使用的引子為 341F：CCTACGGGNGGCWGCAG，805R：GACTACHVGGGTATCTAATCC。這組引子的古菌涵蓋率有偏差風險 [1]；本次古菌占比 3.37% 是擴增後序列比例，不能當成真實細胞比例，也不宜據此認定古菌不足。古菌內部的 76.04% 同樣是本次方法檢出的相對結構。

報告所列「屬級分類率 95.20%」以 ASV 數計算，且包含不確定分類名稱。若把名稱含 UNCLASSIFIED 或 Incertae_Sedis 的屬級項目單獨標示，其序列合計 20,528，占全部 32.81%。另有 RBG-16-49-21 等環境代號，不能視為已知培養菌。物種欄中的 metagenome、uncultured 與 UNCLASSIFIED 不是已確證物種；短片段 16S 的物種名亦需額外驗證。

## 4. 群落結構與食品污泥降解

| 菌門／菌屬 | 全部序列占比 | 生物學解讀與限制 |
| --- | --- | --- |
| Bacillota（舊稱 Firmicutes） | 44.03% | 含多種發酵及共營養細菌；菌門比例不能換算成水解效率 |
| Bacteroidota | 16.27% | 含常見有機物降解及發酵類群；本樣本仍有不少分類未明項目 |
| Cloacimonadota | 10.68% | 值得關注的未充分培養類群；部分成員與胺基酸代謝及共營養丙酸氧化有關 [2] |
| Pseudomonadota（舊稱 Proteobacteria） | 9.06% | 組成多樣，不能整門指定為單一功能 |
| Enterococcus | 12.16% | 常見乳酸發酵相關類群；高比例可反映槽內族群或持續進料 DNA，不能推定酸化失衡 |
| Streptococcus | 7.94% | 同樣提供發酵相關線索；應配合乳酸、VFA、pH 及進料菌相 |
| Brachymonas | 6.33% | 不宜逕列為核心厭氧產甲烷菌或 DIET 菌；需比對進料及活性資料，不能據此宣稱漏氧或反硝化 |
| Fastidiosipila | 2.63% | 在消化槽研究中有與乙酸、丁酸形成相關的推論 [3]；本樣本功能尚未實測 |
| Proteiniclasticum | 0.67% | 已培養代表菌可利用蛋白胨與多種胺基酸並形成有機酸 [4]；屬級檢出支持高氮原料降解的研究假說 |
| Aminobacterium | 0.41% | 可列為胺基酸轉換的追蹤候選，不能由 DNA 豐度估計氨釋放速率 |
| Syntrophomonas | 0.66% | 已知代表菌可共營養氧化丁酸等脂肪酸 [5]；存在不代表當下正在進行該反應 |
| Desulfovibrio | 1.13% | 可追蹤硫酸鹽還原、硫化物及共營養互作；角色取決於可用電子受體等條件 |

Enterococcus 與 Streptococcus 合計 20.10%，可作為後續「進料帶入與槽內選汰」的比較重點。即使產酸菌比例高，也可能與穩定的下游耗酸共同存在，不能把高比例本身視為不穩定指標。DNA 亦可能來自不活躍或已死亡細胞。

Cloacimonadota 共有 6,678 reads，其中 UNCLASSIFIED_8 為 3,500、Incertae_Sedis_6 為 3,106，兩項合計占該菌門 98.92%。2026 年的原始研究以基因體及轉錄體提出這個菌門可能有替代型丙酸氧化途徑 [2]。這使其成為本槽值得追蹤的候選族群，但不能把文獻中的代謝功能直接指定給本樣本的未分類序列。

RBG-16-49-21（3.27%）等環境分支需保留原始譜系，不能僅因物種欄出現 uncultured_Leptospira 就解讀為特定病原。Enterococcus 等分類結果同樣不構成存活病原的確認。

## 5. 產甲烷古菌：最清楚的群落訊號

| 菌屬 | Reads | 占全部序列 | 占本次古菌序列 | 途徑解讀 |
| --- | --- | --- | --- | --- |
| Methanosarcina | 1,603 | 2.56% | 76.04% | 屬內包含乙酸、甲基化合物與 H2/CO2 利用能力不同的物種；不可將全屬指定為單一路徑 [6] |
| Methanothrix（常見舊名 Methanosaeta） | 164 | 0.26% | 7.78% | 支持乙酸利用型產甲烷菌存在；不能由比例推估乙酸裂解通量 |
| Methanospirillum | 123 | 0.20% | 5.83% | 氫營養／部分成員可利用甲酸的產甲烷菌線索 |
| Methanobrevibacter | 123 | 0.20% | 5.83% | 氫營養型產甲烷菌線索 |
| Methanobacterium | 95 | 0.15% | 4.51% | 氫營養型產甲烷菌線索 |
| 合計 | 2,108 | 3.37% | 100% | 分母為序列數，非細胞數或甲烷產量 |

Methanosarcina 與 Methanothrix 的序列比約 9.77：1。可以說「本次檢出的產甲烷古菌以 Methanosarcina 為優勢菌屬」，不能說「76% 的甲烷由 Methanosarcina 產生」。另外三個氫營養相關屬合計 341 reads，占古菌 16.18%；這不包含可能具有氫營養能力的 Methanosarcina 成員，亦非氫營養途徑的實際占比。

## 6. 高氮馴養、SAO 與活性碳：目前證據到哪裡？

**高氮耐受：與操作背景相容，尚未量化。** 高氮食品污泥不等於槽內已達高游離氨。需要同日 TAN、pH 和溫度，才能估計 NH3-N 暴露。穩定產氣顯示系統在既有操作條件下可運作，但沒有負荷、氨濃度和未馴養對照，不能把穩定歸因於特定耐氨菌或馴養機制。

**SAO：可以提出假說，不能宣稱已成主路徑。** 高氨環境中，乙酸可先由 SAO 菌氧化為 CO2 與 H2／甲酸，再由產甲烷菌消耗，原始研究已有這種合作的基因體與表現證據 [7]。本樣本有氫營養相關產甲烷菌，但典型 SAO 候選屬 Tepidanaerobacter 僅 8 reads（0.0128%），且未檢出名為 Syntrophaceticus、Thermacetogenium、Methanoculleus 的屬級項目。低豐度、引子偏差與未分類群仍可能遮蔽功能，因此既不能證實 SAO 主導，也不能排除 SAO 存在。Syntrophomonas 不應直接當成 SAO 菌的替代證據。

**DIET：具研究合理性，缺乏本槽直接證據。** 活性碳在特定共培養條件下可促進電子傳遞 [8]，但該文獻的顆粒活性碳與本次酸洗粉末椰殼碳不同。本樣本有 Methanosarcina、Methanothrix；屬級表沒有名為 Geobacter 的項目。菌名的有無都不能單獨證實或否定 DIET。需有材料對照、電性／表面分析及功能或活性證據，SEM 附著影像本身亦不能證明電子傳遞。

**酸洗效果：尚不能歸因。** 檸檬酸處理可能改變灰分、表面化學、吸附與微量元素釋出，但方向取決於處理條件。未提供未酸洗碳、洗滌程度、碳材 pH、導電度、灰分、元素與吸附試驗，因此不能宣稱酸洗提升導電性、移除抑制物或改善氨吸附。若洗滌不完全，殘餘檸檬酸亦是需控制的碳源與 pH 因子。

## 7. 功能預測與報告缺件

PICRUSt2、Tax4Fun2、FAPROTAX 都是由分類或 16S 序列推估的功能，並未量測實際基因、RNA、酵素或代謝通量。單一樣本不適合比較處理效果，亦不能執行有意義的組間差異或共現網絡分析。

原報告 FAPROTAX 首五列為：乙酸裂解產甲烷 164、甲基歧化產甲烷 1,603、甲酸利用產甲烷 123、H2/CO2 產甲烷 1,944，以及 methanotrophy 6。這些是被功能資料庫分配的 reads，同一類群可以同時被分進不同功能，不能加成 100% 或當成甲烷來源比例。其中 1,944 恰好等於 Methanosarcina 與另三個氫營養相關屬的 reads 合計，提示可能有功能重疊；但缺少貢獻分解表，不能確證每一筆的指派來源。乙酸裂解欄僅列 164，也不能據此宣稱乙酸途徑很少、氫營養途徑絕對主導。methanotrophy 6 亦不能證明槽內有可量化的甲烷氧化。

附件 ZIP 沒有報告文字所引用的完整 data/07-Function 輸出，只有網頁中的示例列；亦缺 weighted NSTI、完整 KO／EC／pathway 表、FAPROTAX 完整表和貢獻分解。因此本次沒有將示例列誤當完整功能結果，也沒有產製功能途徑排名。建議向定序公司索取完整功能資料、ASV 分類信心值、分類器與引子涵蓋說明，以及 FASTQ 原始檔。

## 8. 產氣率與 5% 活性碳的計算基準

650–700 L-biogas/kg-VS 是總沼氣率，不能直接等同甲烷產率或與標準狀態 BMP 的甲烷產率比較。需確認是 VS_added 或 VS_removed、碳材是否計入 VS、氣體是否乾燥且換算標準溫壓，以及是否有空白扣除。甲烷產率應以相同基準的總沼氣率乘以實測甲烷體積分率。

若「5%」指乾燥活性碳占總進料濕重，則每 100 kg 混合進料含約 5 kg 碳。若其餘 95 kg 污泥的 TS 是 15%，污泥乾物為 14.25 kg，混合後 TS 約 19.25%，其中碳占總乾物約 25.97%。另一種情境是加碳後混合物 TS 已為 15%，則碳占總乾物約 33.33%。以上只是兩種明示假設的質量平衡，不是對實際配方的認定。若 5% 指乾重基準，則必須改算。

因此建議將污泥與活性碳分開量測 TS/VS，釐清碳材在 VS 灼燒測定中的損失，不宜直接把混合進料 VS 全視為可生物降解基質。碳會影響表觀固體含量及 VS 正規化，這是解讀產氣率及放大成本的重要前提。缺乏 VS/TS、進料量和有效容積，現階段不能計算實際 OLR 或容積產氣率。

## 9. 下一步驗證與可用於報告的表述

| 優先順序 | 建議補充 | 可回答的問題 |
| --- | --- | --- |
| 先補操作紀錄 | 採樣當日及前後的 pH、溫度、TAN、VFA 分項、鹼度、CH4/CO2、進料 VS、氣量與標準化方式 | 當時是否有氨／酸壓力，產氣率與負荷如何連動 |
| 分辨進料與槽內菌 | 同步採原料、接種源／槽內混合物、出料，並作不同穩定期時間點追蹤 | 高比例發酵菌是否主要由進料帶入，菌相是否持續穩定 |
| 驗證產甲烷能力 | 古菌專一引子、mcrA qPCR，必要時 RT-qPCR，配合乙酸及 H2/CO2 活性試驗 | 產甲烷菌絕對基因量及活性；qPCR 本身仍非代謝通量 |
| 區分碳材效應 | 未加碳、未酸洗碳、酸洗碳；一致的污泥 VS 負荷與操作條件 | 碳材及酸洗是否改善產氣、耗酸或抗氨能力 |
| 避免混淆因子 | 酸洗後充分洗滌並記錄，必要時設殘餘檸檬酸控制；材料組平行比較 | 是否為酸／額外碳源或材料差異造成效果 |
| 機制研究 | 對 SAO 採用同位素乙酸追蹤與功能分析；對 DIET 結合導電與非導電載體對照、電性及活性證據 | 分辨乙酸裂解／SAO，以及吸附、附著與電子傳遞貢獻 |

比較處理效果應有獨立反應器生物重複；同一反應器的多次採樣屬時間序列，不能冒充獨立反應器重複。材料組應保持等量污泥 VS，另記碳材劑量與固體負荷。

建議成果文字：「於高氮食品污泥與檸檬酸酸洗椰殼活性碳共同進料、穩定產沼氣之操作條件下，出料沼渣之 16S rRNA 基因定序顯示群落包含多種發酵與共營養代謝相關類群，產甲烷古菌以 Methanosarcina 為主要檢出菌屬，占古菌序列 76.04%。此群落結構提供後續探討有機酸轉換與產甲烷途徑的候選對象；酸洗活性碳的效益及 SAO／DIET 之參與，仍需對照試驗與功能性量測驗證。」

## 文獻來源

[1] Hugerth et al. (2014). DegePrime, a Program for Degenerate Primer Design for Broad-Taxonomic-Range PCR in Microbial Ecology Studies. [原始研究](https://doi.org/10.1128/AEM.01403-14)

[2] Phylum-wide propionate degradation and its potential connection to poly-gamma-glutamate biosynthesis in Candidatus Cloacimonadota phylum (2026). [原始研究](https://doi.org/10.1093/ismejo/wrag055)

[3] Inoculum Source Determines Acetate and Lactate Production during Anaerobic Digestion of Sewage Sludge and Food Waste (2020). [原始研究](https://pmc.ncbi.nlm.nih.gov/articles/PMC7175179/)

[4] Zhang et al. (2010). Proteiniclasticum ruminis gen. nov., sp. nov., a strictly anaerobic proteolytic bacterium isolated from yak rumen. [原始研究](https://doi.org/10.1099/ijs.0.011759-0)

[5] McInerney et al. (1981). Syntrophomonas wolfei gen. nov. sp. nov., an Anaerobic, Syntrophic, Fatty Acid-Oxidizing Bacterium. [原始研究](https://doi.org/10.1128/aem.41.4.1029-1039.1981)

[6] Galagan et al. (2002). The Genome of M. acetivorans Reveals Extensive Metabolic and Physiological Diversity. [原始研究](https://genome.cshlp.org/content/12/4/532)

[7] Weng et al. (2024). Catabolism and interactions of syntrophic propionate- and acetate oxidizing microorganisms under mesophilic, high-ammonia conditions. [原始研究](https://doi.org/10.3389/fmicb.2024.1389257)

[8] Liu et al. (2012). Promoting direct interspecies electron transfer with activated carbon. [原始研究](https://doi.org/10.1039/C2EE22459C)
