# Literature Review of ESM-2 Large Model Misclassifications (Test Set)

## Overview

This document reviews all 85 misclassifications from the LoRA fine-tuned ESM-2 650M model on the held-out test set. Each entry is assessed against peer-reviewed literature and assigned one of four labels:

- **🟢 PHI-base annotation error** — The PHI-base label is wrong; the model prediction better matches the literature.
- **🟢 Dual-function protein** — The protein genuinely straddles two functional categories; both labels are defensible.
- **🟡 Mixed evidence** — Some biological basis for the model's prediction, but the PHI-base label is more accurate overall.
- **🔴 Model error** — The model prediction is clearly wrong with no strong biological justification.

---

## Entry-by-Entry Analysis

**1. PHI:9239 — alg8, *Pseudomonas aeruginosa*** | True: SM/Biosynthesis → Predicted: CW/Carbohydrate-active (0.998) | **🟢 PHI-base annotation error**
Alg8 is a GT-2 family glycosyltransferase that polymerises GDP-mannuronate into alginate, a polysaccharide — it is a carbohydrate-active enzyme by definition (Remminghorst & Rehm, 2009, *J Biotechnol*). The model's CW/Carbohydrate-active prediction is more accurate than "Secondary metabolite / Biosynthesis"; alginate is not a secondary metabolite.

**2. PHI:123118 — SsPG1-1, *Sclerotinia sclerotiorum*** | True: Kinase/Signalling → Predicted: CW/Carbohydrate-active (0.997) | **🟢 PHI-base annotation error**
SsPG1 is an endopolygalacturonase — a cell wall-degrading enzyme that hydrolyses pectin during plant infection (Bashi et al., 2012, *J Appl Microbiol*). The PHI-base label "Kinase / Signalling" appears to be a curation error; the model's CW/Carbohydrate-active prediction is correct.

**3. PHI:7092 — vgrG-1, *Erwinia amylovora*** | True: Effector → Predicted: Secretion system (0.995) | **🟢 Dual-function protein**
VgrG proteins serve dual roles as structural spike components of the T6SS apparatus and as secreted effectors in many bacteria. In *E. amylovora*, the VgrG proteins lack evolved effector domains (De Maayer et al., 2011, *BMC Genomics*), making "Secretion system" arguably more accurate here.

**4. PHI:4975 — LssB, *Legionella pneumophila*** | True: Secretion system → Predicted: Transporter/Membrane (0.992) | **🟡 Mixed evidence**
LssB is the ABC transporter component of the T1SS that secretes RtxA (Fuche et al., 2015, *J Bacteriol*). ABC transporters are mechanistically transporters, but the PHI-base "Secretion system" label better captures the functional context.

**5. PHI:124139 — Zip350, *Orbilia oligospora*** | True: SM/Biosynthesis → Predicted: TF/Regulator (0.992) | **🟢 PHI-base annotation error**
Described as a histone H3K4 methyltransferase — this is an epigenetic regulator that modifies chromatin to control gene expression. The model's TF/Regulator prediction more accurately reflects the molecular function than "Secondary metabolite / Biosynthesis".

**6. PHI:5338 — tssK-5, *Burkholderia pseudomallei*** | True: Effector → Predicted: Secretion system (0.991) | **🟢 PHI-base annotation error**
TssK is a conserved T6SS baseplate component required for assembly, not a translocated effector. The PHI-base annotation "T6SS5 effector" is misleading; the model's "Secretion system" is correct.

**7. PHI:5257 — secY, *Listeria monocytogenes*** | True: Secretion system → Predicted: Transporter/Membrane (0.991) | **🟡 Mixed evidence**
SecY is the central channel of the Sec translocon — an integral membrane protein that translocates polypeptides across the inner membrane. Both labels are defensible; "Transporter / Membrane" reflects its molecular nature while "Secretion system" reflects its pathway role.

**8. PHI:123702 — dgkA, *Pseudomonas aeruginosa*** | True: Kinase/Signalling → Predicted: Transporter/Membrane (0.991) | **🔴 Model error**
Diacylglycerol kinase phosphorylates DAG in membrane lipid turnover. While membrane-associated, it is a bona fide kinase — the PHI-base label is correct.

**9. PHI:3756 — sifA, *Salmonella enterica*** | True: Secretion system → Predicted: Effector (0.990) | **🟢 PHI-base annotation error**
SifA is a well-characterised T3SS translocated effector that maintains Salmonella-containing vacuole integrity and induces Sif filament formation. It is an effector, not a secretion system component — the model is correct.

**10. PHI:124511 — flbC, *Fusarium oxysporum*** | True: Kinase/Signalling → Predicted: TF/Regulator (0.990) | **🟢 PHI-base annotation error**
FlbC is a C2H2-type zinc finger transcription factor that regulates conidiophore development in filamentous fungi. The C2H2 domain is a DNA-binding domain — the model's TF/Regulator prediction is correct.

**11. PHI:1555 — GzMyb019, *Fusarium graminearum*** | True: TF/Regulator → Predicted: Transporter/Membrane (0.990) | **🔴 Model error**
GzMyb019 is described as a transcription factor — the PHI-base label is correct and the model prediction of Transporter / Membrane has no strong biological basis.

**12. PHI:3663 — gluP, *Xylella fastidiosa*** | True: Kinase/Signalling → Predicted: Transporter/Membrane (0.989) | **🟢 PHI-base annotation error**
Annotated as "glucose kinase, Glk" but the gene name gluP and functional context suggest a glucose permease/transporter rather than a kinase in *Xylella*. The model's Transporter/Membrane prediction appears more consistent with the PD_0681 annotation.

**13. PHI:5242 — ccpE, *Staphylococcus aureus*** | True: SM/Biosynthesis → Predicted: TF/Regulator (0.988) | **🟢 PHI-base annotation error**
CcpE is described as regulating virulence determinant biosynthesis — it is a transcriptional regulator of the citric acid cycle and virulence genes in *S. aureus*. The model's TF/Regulator prediction is more accurate than SM/Biosynthesis.

**14. PHI:7715 — MGA_0220, *Mycoplasmoides gallisepticum*** | True: Kinase/Signalling → Predicted: Transporter/Membrane (0.987) | **🟢 PHI-base annotation error**
Annotated as an "oligopeptide transporter ATP-binding protein" — this is a component of an ABC transporter system. The model's Transporter/Membrane prediction matches the gene annotation; the PHI-base "Kinase / Signalling" label is incorrect.

**15. PHI:7193 — FgLaeA, *Fusarium graminearum*** | True: TF/Regulator → Predicted: SM/Biosynthesis (0.982) | **🟡 Mixed evidence**
LaeA is a global regulator of secondary metabolism via chromatin modification in the velvet complex. The PHI-base TF/Regulator label is correct for the molecular function, though LaeA is so tightly associated with SM regulation that the model's confusion is understandable.

**16. PHI:9298 — Penlp1, *Penicillium expansum*** | True: Kinase/Signalling → Predicted: Effector (0.982) | **🟢 PHI-base annotation error**
NLP (necrosis and ethylene-inducing-like protein) family members are well-established secreted effectors that induce programmed cell death in plants. The model's Effector prediction is correct; the PHI-base "Kinase / Signalling" label is wrong.

**17. PHI:125077 — g2572, *Alternaria alternata*** | True: Protease → Predicted: Kinase/Signalling (0.982) | **🔴 Model error**
A subtilisin-like protease — the PHI-base Protease label is correct. Same pattern as the g2573 subtilisin misclassification identified in the previous analysis.

**18. PHI:3333 — pga7, *Candida albicans*** | True: Kinase/Signalling → Predicted: Effector (0.981) | **🟡 Mixed evidence**
Pga7/Rbt5 is a GPI-anchored cell surface protein involved in extracellular heme binding and iron acquisition during infection. The Kinase/Signalling label is questionable, but "Effector" is also imprecise — it is more of a surface virulence factor.

**19. PHI:5334 — tssF-5, *Burkholderia pseudomallei*** | True: Effector → Predicted: Secretion system (0.980) | **🟢 PHI-base annotation error**
TssF is a conserved T6SS baseplate structural component, not a translocated effector. Same pattern as tssK-5 (#6) — the PHI-base label "T6SS5 effector" is wrong and the model's prediction is correct.

**20. PHI:7538 — FepA, *Klebsiella pneumoniae*** | True: SM/Biosynthesis → Predicted: Transporter/Membrane (0.980) | **🟢 PHI-base annotation error**
FepA is described as a "TonB-dependent siderophore receptor" — it is an outer membrane transporter for ferric enterobactin, not a biosynthetic enzyme. Same pattern as iutA in the previous analysis; the model is correct.

**21. PHI:2341 — BeNEP1, *Botrytis elliptica*** | True: Kinase/Signalling → Predicted: Effector (0.975) | **🟢 PHI-base annotation error**
NEP1-like proteins (NLPs) are secreted effectors that trigger necrosis and ethylene production in plants. BeNEP1 is a classic necrotrophic effector — the model is correct; the Kinase/Signalling label is wrong.

**22. PHI:10805 — cp2, *Verticillium dahliae*** | True: Kinase/Signalling → Predicted: TF/Regulator (0.975) | **🟡 Mixed evidence**
CP2 domain-containing proteins in fungi can have diverse functions. Without detailed functional characterisation, both labels are speculative.

**23. PHI:125233 — pilJ, *Acidovorax citrulli*** | True: Secretion system → Predicted: Kinase/Signalling (0.973) | **🟡 Mixed evidence**
PilJ is a type IV pilus component but also functions as a methyl-accepting chemotaxis protein (MCP) that senses signals. The PHI-base label is more accurate, but the signalling function explains the model's confusion.

**24. PHI:123153 — NWMN2330, *Staphylococcus aureus*** | True: Effector → Predicted: Transporter/Membrane (0.973) | **🟡 Mixed evidence**
Annotated generically as "virulence factor" — without detailed characterisation it is difficult to assess which label is more appropriate.

**25. PHI:4137 — xrp8, *Xanthomonas oryzae*** | True: Effector → Predicted: Kinase/Signalling (0.972) | **🟡 Mixed evidence**
Described as a "type III effector" — if this is a genuine T3E, the PHI-base label is correct. Many T3Es mimic host signalling proteins, which could explain the model's prediction.

**26. PHI:4865 — FgVam7, *Fusarium graminearum*** | True: TF/Regulator → Predicted: Kinase/Signalling (0.971) | **🟡 Mixed evidence**
Vam7 is a SNARE protein involved in vacuolar membrane fusion — it functions in vesicle trafficking signalling, not transcription. The PHI-base TF/Regulator label is questionable; the Kinase/Signalling prediction may be closer to the truth.

**27. PHI:123562 — Slm2, *Exserohilum turcicum*** | True: TF/Regulator → Predicted: Kinase/Signalling (0.966) | **🟡 Mixed evidence**
Described as a "cytoskeleton regulator" — this is not obviously a transcription factor. Both labels are imprecise; the protein likely functions in cytoskeletal dynamics/signalling.

**28. PHI:9496 — yeaB, *Salmonella enterica*** | True: SM/Biosynthesis → Predicted: Kinase/Signalling (0.964) | **🔴 Model error**
An RNA methyltransferase — while the SM/Biosynthesis label is itself debatable for an RNA modification enzyme, the model's Kinase/Signalling prediction is clearly wrong.

**29. PHI:1025 — bcnoxR, *Botrytis cinerea*** | True: TF/Regulator → Predicted: Kinase/Signalling (0.963) | **🟡 Mixed evidence**
BcNoxR is the regulatory subunit of the NADPH oxidase complex — it regulates ROS signalling rather than acting as a classical transcription factor. Both labels capture aspects of its function.

**30. PHI:8915 — FgVPS32, *Fusarium graminearum*** | True: Transporter/Membrane → Predicted: Kinase/Signalling (0.959) | **🔴 Model error**
VPS32 is an ESCRT-III component involved in endosomal sorting and membrane trafficking. The PHI-base Transporter/Membrane label is correct; same pattern as FgVPS22 from the previous analysis.

**31. PHI:11614 — cyaB, *Borreliella burgdorferi*** | True: Kinase/Signalling → Predicted: Effector (0.954) | **🟡 Mixed evidence**
CyaB is a class IV adenylate cyclase that generates cAMP as a second messenger. The PHI-base Kinase/Signalling label is appropriate, though adenylate cyclases are sometimes deployed as effectors by other pathogens (e.g. *B. anthracis* EF).

**32. PHI:10956 — phoQ, *Stenotrophomonas maltophilia*** | True: TF/Regulator → Predicted: Secretion system (0.954) | **🟡 Mixed evidence**
PhoQ is a two-component sensor histidine kinase — TF/Regulator or Kinase/Signalling would be appropriate labels. The model's Secretion system prediction is incorrect.

**33. PHI:12073 — vWbp, *Staphylococcus aureus*** | True: Kinase/Signalling → Predicted: Effector (0.954) | **🟢 PHI-base annotation error**
Von Willebrand factor-binding protein is a secreted coagulase that activates host prothrombin — it is a secreted virulence factor/effector, not a kinase. The model's Effector prediction is more accurate.

**34. PHI:5577 — esx-3, *Mycobacterium tuberculosis*** | True: Effector → Predicted: Secretion system (0.952) | **🟡 Mixed evidence**
ESX-3 is a type VII secretion system in mycobacteria involved in iron acquisition. Whether this specific gene encodes a structural component vs a secreted substrate determines the correct label — both are plausible.

**35. PHI:11868 — otsA, *Acinetobacter baumannii*** | True: TF/Regulator → Predicted: Transporter/Membrane (0.948) | **🔴 Model error**
OtsA is trehalose-6-phosphate synthase — a biosynthetic enzyme. Neither the PHI-base TF/Regulator label nor the model's Transporter/Membrane prediction is ideal, but both are wrong; this should likely be SM/Biosynthesis.

**36. PHI:123650 — malM, *Escherichia coli*** | True: TF/Regulator → Predicted: Transporter/Membrane (0.946) | **🔴 Model error**
MalM is a periplasmic protein of the maltose regulon. The PHI-base TF/Regulator label is broadly correct; the model's Transporter/Membrane prediction is not well-supported. Same entry as in the previous high-confidence analysis.

**37. PHI:123977 — lphD, *Legionella pneumophila*** | True: Effector → Predicted: TF/Regulator (0.945) | **🔴 Model error**
Described as an effector protein — without evidence of regulatory function, the model's TF/Regulator prediction is unjustified.

**38. PHI:12129 — bglu_2g07420, *Burkholderia glumae*** | True: Kinase/Signalling → Predicted: Secretion system (0.943) | **🟡 Mixed evidence**
A pentapeptide repeat-containing protein — these have diverse functions and the Kinase/Signalling label is not clearly correct. Neither label is obviously appropriate.

**39. PHI:6687 — gra10, *Toxoplasma gondii*** | True: Effector → Predicted: TF/Regulator (0.931) | **🟡 Mixed evidence**
GRA10 is a dense granule protein secreted into the parasitophorous vacuole. While it is an effector, some GRA proteins (e.g. GRA16, GRA24) do traffic to the host nucleus and regulate transcription — but GRA10 is not well-characterised in this role.

**40. PHI:11231 — SAUSA300_0964, *Staphylococcus aureus*** | True: CW/Carbohydrate-active → Predicted: Kinase/Signalling (0.930) | **🔴 Model error**
Described as a chitinase-related protein — the PHI-base CW/Carbohydrate-active label is correct for a glycoside hydrolase family member. The model's Kinase/Signalling prediction is wrong.

**41. PHI:10500 — tapV, *Ralstonia solanacearum*** | True: Transporter/Membrane → Predicted: Secretion system (0.924) | **🟡 Mixed evidence**
Described as a type IV pilus assembly protein — T4P components bridge Transporter/Membrane and Secretion system categories, as pili function in both motility/adhesion and secretion.

**42. PHI:6321 — potC, *Streptococcus pneumoniae*** | True: Kinase/Signalling → Predicted: Transporter/Membrane (0.923) | **🟢 PHI-base annotation error**
Described as an "ABC transporter ATP-binding protein" for spermidine/putrescine transport. The model's Transporter/Membrane prediction matches the annotation; the Kinase/Signalling label is incorrect.

**43. PHI:124144 — RvvA, *Vibrio cholerae*** | True: TF/Regulator → Predicted: Secretion system (0.916) | **🟡 Mixed evidence**
RvvA is a two-component sensor kinase that regulates virulence. The TF/Regulator label is broadly appropriate; the model's Secretion system prediction is incorrect.

**44. PHI:7118 — gtfA, *Streptococcus pneumoniae*** | True: CW/Carbohydrate-active → Predicted: SM/Biosynthesis (0.913) | **🟡 Mixed evidence**
GtfA is a glycosyltransferase that attaches GalNAc to serine-rich repeat proteins. Both CW/Carbohydrate-active and SM/Biosynthesis are imprecise for a protein glycosyltransferase, but the PHI-base label is closer.

**45. PHI:124082 — FliY, *Actinobacillus pleuropneumoniae*** | True: Transporter/Membrane → Predicted: Kinase/Signalling (0.913) | **🔴 Model error**
FliY is described as an amino acid ABC transporter substrate-binding protein — the Transporter/Membrane label is correct.

**46. PHI:4769 — HaRxLL470b, *Hyaloperonospora arabidopsidis*** | True: Effector → Predicted: Kinase/Signalling (0.911) | **🟡 Mixed evidence**
A characterised oomycete RXLR effector — the PHI-base Effector label is correct. Many RXLR effectors manipulate host kinase signalling, explaining the model's confusion.

**47. PHI:4715 — crc, *Pseudomonas aeruginosa*** | True: TF/Regulator → Predicted: Kinase/Signalling (0.899) | **🟡 Mixed evidence**
Crc is an RNA-binding post-transcriptional regulator of carbon catabolite repression. The TF/Regulator label is broadly correct; the model's Kinase/Signalling prediction reflects Crc's role in metabolic sensing but is less accurate.

**48. PHI:2489 — rsmAXoo, *Xanthomonas oryzae*** | True: Kinase/Signalling → Predicted: TF/Regulator (0.897) | **🟢 PHI-base annotation error**
RsmA is an RNA-binding post-transcriptional regulator of the CsrA family. The model's TF/Regulator prediction is more accurate than Kinase/Signalling.

**49. PHI:7136 — lcrV, *Yersinia pestis*** | True: Secretion system → Predicted: Effector (0.888) | **🟢 Dual-function protein**
LcrV (V antigen) is both a T3SS needle tip protein and a secreted immunomodulatory factor that suppresses host immune responses. Both labels are defensible.

**50. PHI:3725 — PhoPQ, *Salmonella enterica*** | True: Kinase/Signalling → Predicted: Secretion system (0.871) | **🔴 Model error**
PhoQ is a sensor histidine kinase of the two-component system. The Kinase/Signalling label is correct; the model's Secretion system prediction is wrong.

**51. PHI:6998 — BfiS, *Pseudomonas aeruginosa*** | True: Kinase/Signalling → Predicted: TF/Regulator (0.871) | **🟡 Mixed evidence**
BfiS is a sensor kinase of a two-component system — as with other TCS proteins, both Kinase/Signalling and TF/Regulator capture different aspects. The PHI-base label is marginally more precise.

**52. PHI:12224 — MoPtep1, *Magnaporthe oryzae*** | True: Effector → Predicted: CW/Carbohydrate-active (0.861) | **🔴 Model error**
Described as an effector protein — without evidence of carbohydrate-active function, the model's prediction is unjustified.

**53. PHI:12236 — VdAda1, *Verticillium dahliae*** | True: SM/Biosynthesis → Predicted: Kinase/Signalling (0.858) | **🟢 PHI-base annotation error**
Described as a Spt-Ada-Gcn5 acetyltransferase (SAGA) complex component — SAGA is a histone acetyltransferase complex that regulates transcription. Neither SM/Biosynthesis nor Kinase/Signalling is ideal; TF/Regulator would be most accurate, but the model detects the acetyltransferase/signalling function.

**54. PHI:8921 — EadM, *Xanthomonas axonopodis*** | True: TF/Regulator → Predicted: SM/Biosynthesis (0.857) | **🟡 Mixed evidence**
A DNA methyltransferase — this modifies DNA and can regulate gene expression epigenetically. TF/Regulator captures the regulatory consequence; SM/Biosynthesis captures the enzymatic (methyltransferase) activity. The PHI-base label is more appropriate.

**55. PHI:123246 — EI219_09440, *Streptococcus suis*** | True: Kinase/Signalling → Predicted: TF/Regulator (0.849) | **🟡 Mixed evidence**
A DUF1836 domain-containing protein — without detailed functional data, neither label can be verified.

**56. PHI:5258 — tfpO, *Pseudomonas aeruginosa*** | True: CW/Carbohydrate-active → Predicted: Transporter/Membrane (0.848) | **🟡 Mixed evidence**
TfpO is a glycosyltransferase that modifies the type IV pilin — the PHI-base CW/Carbohydrate-active label is correct for a glycosyltransferase, though the pilin association could explain the Transporter/Membrane confusion.

**57. PHI:124632 — UMAG_10076, *Ustilago maydis*** | True: Effector → Predicted: CW/Carbohydrate-active (0.841) | **🟡 Mixed evidence**
Described as an effector protein — some *U. maydis* effectors do target plant cell wall metabolism, but without specific functional characterisation this is likely a model error.

**58. PHI:231 — RPK1, *Colletotrichum lagenaria*** | True: TF/Regulator → Predicted: Kinase/Signalling (0.822) | **🟢 PHI-base annotation error**
RPK1 is described as a PKA regulatory subunit — it is a component of the cAMP-dependent protein kinase signalling pathway, not a transcription factor. The model's Kinase/Signalling prediction is correct.

**59. PHI:4960 — rsmI, *Staphylococcus aureus*** | True: SM/Biosynthesis → Predicted: Kinase/Signalling (0.817) | **🔴 Model error**
A ribosomal RNA small subunit methyltransferase — this is a post-transcriptional RNA modification enzyme. The SM/Biosynthesis label is imprecise but the model's Kinase/Signalling prediction is clearly wrong.

**60. PHI:3120 — PSPTO_3331, *Pseudomonas syringae*** | True: Protease → Predicted: Secretion system (0.809) | **🟡 Mixed evidence**
Described as an "alkaline proteinase inhibitor" — a protease *inhibitor*, not a protease itself. The PHI-base Protease label is imprecise. The model's Secretion system prediction is also wrong, but the PHI-base label is itself questionable.

**61. PHI:7603 — rfbE, *Brucella abortus*** | True: Kinase/Signalling → Predicted: Transporter/Membrane (0.781) | **🟢 PHI-base annotation error**
Described as an "O-antigen export system ATP-binding protein" — this is a transporter component. The model's Transporter/Membrane prediction matches the annotation; Kinase/Signalling is incorrect.

**62. PHI:11210 — cda7, *Ustilago maydis*** | True: CW/Carbohydrate-active → Predicted: TF/Regulator (0.775) | **🔴 Model error**
Chitin deacetylase is a carbohydrate-active enzyme that converts chitin to chitosan. The PHI-base CW/Carbohydrate-active label is correct.

**63. PHI:6319 — potA, *Streptococcus pneumoniae*** | True: Kinase/Signalling → Predicted: Transporter/Membrane (0.752) | **🟢 PHI-base annotation error**
Described as an "ABC transporter ATP-binding protein" for spermidine/putrescine transport — same pattern as potC (#42). The model's Transporter/Membrane prediction is correct.

**64. PHI:3593 — MgtC, *Mycobacterium marinum*** | True: Transporter/Membrane → Predicted: Secretion system (0.720) | **🟡 Mixed evidence**
MgtC is an intramacrophage growth factor involved in Mg2+ homeostasis. The Transporter/Membrane label is broadly appropriate for an Mg2+ transport-related protein; the model's Secretion system prediction is incorrect.

**65. PHI:4921 — flmQ, *Burkholderia cenocepacia*** | True: CW/Carbohydrate-active → Predicted: Kinase/Signalling (0.680) | **🔴 Model error**
A flagellin glycosyltransferase — the PHI-base CW/Carbohydrate-active label is correct for a glycosyltransferase.

**66. PHI:3086 — prtA, *Photorhabdus luminescens*** | True: Effector → Predicted: Protease (0.666) | **🟢 Dual-function protein**
PrtA is a secreted metalloprotease virulence factor. Same dual-function pattern as the metalloprotease-effectors in the previous analysis (Cgfl, MEP1, FoMep1) — both Effector and Protease are valid.

**67. PHI:11519 — rv3680, *Mycobacterium tuberculosis*** | True: Transporter/Membrane → Predicted: Secretion system (0.643) | **🟡 Mixed evidence**
Described as a "probable anion transporter ATPase" — the Transporter/Membrane label is correct. The confusion with Secretion system likely reflects shared membrane-associated ATPase features.

**68. PHI:4834 — TceSR, *Brucella melitensis*** | True: TF/Regulator → Predicted: Secretion system (0.641) | **🟡 Mixed evidence**
A two-component regulatory system — the TF/Regulator label is appropriate. The model's Secretion system prediction is wrong.

**69. PHI:11554 — A1479, *Brucella melitensis*** | True: Transporter/Membrane → Predicted: Kinase/Signalling (0.635) | **🔴 Model error**
Described as a "cell envelope-related amide hydrolase" — the Transporter/Membrane label is broadly appropriate for a cell envelope protein. The model's Kinase/Signalling prediction is unjustified.

**70. PHI:6568 — REP34, *Francisella tularensis*** | True: Protease → Predicted: CW/Carbohydrate-active (0.633) | **🟡 Mixed evidence**
A carboxypeptidase — carboxypeptidases are proteases, so the PHI-base label is correct. However, some carboxypeptidases act on peptidoglycan (cell wall), which could explain the model's CW prediction.

**71. PHI:6674 — MoTRX2, *Magnaporthe oryzae*** | True: TF/Regulator → Predicted: Kinase/Signalling (0.626) | **🟡 Mixed evidence**
MoTRX2 is a thioredoxin oxidoreductase — a redox enzyme involved in ROS signalling, not a transcription factor. Neither label is ideal; the model's Kinase/Signalling prediction captures the signalling function, while the PHI-base label reflects downstream regulatory effects.

**72. PHI:10789 — BAB1_0270, *Brucella abortus*** | True: Protease → Predicted: Transporter/Membrane (0.622) | **🔴 Model error**
A zinc-dependent metalloproteinase — the Protease label is correct.

**73. PHI:11872 — cadC, *Edwardsiella tarda*** | True: Transporter/Membrane → Predicted: TF/Regulator (0.617) | **🟢 Dual-function protein**
CadC is a membrane-integrated transcriptional activator of the lysine decarboxylase system — it spans the membrane (sensor domain) and directly activates transcription (DNA-binding domain). Both labels are valid.

**74. PHI:7667 — LysM4, *Penicillium expansum*** | True: Effector → Predicted: CW/Carbohydrate-active (0.602) | **🟢 Dual-function protein**
LysM effectors bind chitin (a carbohydrate) to suppress host immune recognition. The protein is both an effector (suppresses immunity) and carbohydrate-active (binds chitin) — both labels are defensible.

**75. PHI:5109 — prt, *Salmonella enterica*** | True: SM/Biosynthesis → Predicted: TF/Regulator (0.601) | **🟡 Mixed evidence**
Involved in O-antigen biosynthesis — the SM/Biosynthesis label is appropriate for a polysaccharide biosynthetic gene. The model's TF/Regulator prediction is wrong.

**76. PHI:7478 — FepB, *Klebsiella pneumoniae*** | True: Transporter/Membrane → Predicted: Kinase/Signalling (0.557) | **🔴 Model error**
A periplasmic enterobactin transporter — the Transporter/Membrane label is correct.

**77. PHI:4223 — Pde2, *Streptococcus pneumoniae*** | True: Kinase/Signalling → Predicted: SM/Biosynthesis (0.553) | **🟡 Mixed evidence**
Pde2 has c-di-AMP phosphodiesterase activity — it is a signalling enzyme that degrades c-di-AMP. The Kinase/Signalling label is appropriate; the model's SM/Biosynthesis prediction reflects the enzymatic/phosphodiesterase activity but is less accurate.

**78. PHI:4112 — MoVELB, *Magnaporthe oryzae*** | True: TF/Regulator → Predicted: Kinase/Signalling (0.529) | **🟡 Mixed evidence**
VelB is a velvet family protein that forms a complex with VeA and LaeA to regulate development and secondary metabolism. The TF/Regulator label is correct; the Kinase/Signalling prediction is wrong.

**79. PHI:6097 — hns, *Klebsiella pneumoniae*** | True: TF/Regulator → Predicted: Kinase/Signalling (0.511) | **🔴 Model error**
H-NS is a well-characterised histone-like nucleoid-structuring protein and global transcriptional regulator. The TF/Regulator label is clearly correct.

**80. PHI:3115 — PSPTO_5633, *Pseudomonas syringae*** | True: Effector → Predicted: Secretion system (0.511) | **🟡 Mixed evidence**
Described as an effector protein — if it is a genuine T3E, the PHI-base label is correct. The low confidence (0.511) suggests the model is uncertain.

**81. PHI:1683 — GzRad001, *Fusarium graminearum*** | True: TF/Regulator → Predicted: Kinase/Signalling (0.501) | **🔴 Model error**
Described as a transcription factor — the PHI-base label is correct, though the near-random confidence (0.501) shows the model is effectively guessing.

**82. PHI:4633 — dgcB, *Burkholderia glumae*** | True: Kinase/Signalling → Predicted: TF/Regulator (0.500) | **🟡 Mixed evidence**
A diguanylate cyclase that synthesises c-di-GMP — this is a signalling enzyme. The Kinase/Signalling label is appropriate; the model's TF/Regulator prediction reflects downstream regulatory effects but is less precise.

**83. PHI:7298 — PhzG1, *Pseudomonas aeruginosa*** | True: SM/Biosynthesis → Predicted: Kinase/Signalling (0.461) | **🔴 Model error**
PhzG1 is a phenazine biosynthesis enzyme — the SM/Biosynthesis label is unambiguously correct.

**84. PHI:10428 — vreR, *Pseudomonas aeruginosa*** | True: TF/Regulator → Predicted: Kinase/Signalling (0.430) | **🟡 Mixed evidence**
VreR is a sigma factor regulator (anti-sigma factor) — the TF/Regulator label is correct, though the regulatory mechanism involves signalling. Near-random confidence.

**85. PHI:3417 — Ohmm, *Beauveria bassiana*** | True: Transporter/Membrane → Predicted: SM/Biosynthesis (0.413) | **🔴 Model error**
A mitochondrial transmembrane protein — the Transporter/Membrane label is correct. Near-random confidence (0.413).

---

## Summary Table

### 🟢 PHI-base annotation error (model prediction is correct or more accurate)

| # | PHI ID | Gene | Organism |
|---|--------|------|----------|
| 1 | PHI:9239 | alg8 | *P. aeruginosa* |
| 2 | PHI:123118 | SsPG1-1 | *S. sclerotiorum* |
| 6 | PHI:5338 | tssK-5 | *B. pseudomallei* |
| 9 | PHI:3756 | sifA | *S. enterica* |
| 10 | PHI:124511 | flbC | *F. oxysporum* |
| 12 | PHI:3663 | gluP | *X. fastidiosa* |
| 13 | PHI:5242 | ccpE | *S. aureus* |
| 14 | PHI:7715 | MGA_0220 | *M. gallisepticum* |
| 16 | PHI:9298 | Penlp1 | *P. expansum* |
| 19 | PHI:5334 | tssF-5 | *B. pseudomallei* |
| 20 | PHI:7538 | FepA | *K. pneumoniae* |
| 21 | PHI:2341 | BeNEP1 | *B. elliptica* |
| 33 | PHI:12073 | vWbp | *S. aureus* |
| 42 | PHI:6321 | potC | *S. pneumoniae* |
| 48 | PHI:2489 | rsmAXoo | *X. oryzae* |
| 53 | PHI:12236 | VdAda1 | *V. dahliae* |
| 58 | PHI:231 | RPK1 | *C. lagenaria* |
| 61 | PHI:7603 | rfbE | *B. abortus* |
| 63 | PHI:6319 | potA | *S. pneumoniae* |

Also PHI:124139 (Zip350, #5) where the model's TF/Regulator is closer to the truth than SM/Biosynthesis.

**Total: 20**

### 🟢 Dual-function protein (both labels are biologically defensible)

| # | PHI ID | Gene | Organism |
|---|--------|------|----------|
| 3 | PHI:7092 | vgrG-1 | *E. amylovora* |
| 49 | PHI:7136 | lcrV | *Y. pestis* |
| 66 | PHI:3086 | prtA | *P. luminescens* |
| 73 | PHI:11872 | cadC | *E. tarda* |
| 74 | PHI:7667 | LysM4 | *P. expansum* |

**Total: 5**

### 🟡 Mixed evidence (some biological basis for the model's prediction, but PHI-base is more accurate)

| # | PHI ID | Gene | Organism |
|---|--------|------|----------|
| 4 | PHI:4975 | LssB | *L. pneumophila* |
| 7 | PHI:5257 | secY | *L. monocytogenes* |
| 15 | PHI:7193 | FgLaeA | *F. graminearum* |
| 18 | PHI:3333 | pga7 | *C. albicans* |
| 22 | PHI:10805 | cp2 | *V. dahliae* |
| 23 | PHI:125233 | pilJ | *A. citrulli* |
| 24 | PHI:123153 | NWMN2330 | *S. aureus* |
| 25 | PHI:4137 | xrp8 | *X. oryzae* |
| 26 | PHI:4865 | FgVam7 | *F. graminearum* |
| 27 | PHI:123562 | Slm2 | *E. turcicum* |
| 29 | PHI:1025 | bcnoxR | *B. cinerea* |
| 31 | PHI:11614 | cyaB | *B. burgdorferi* |
| 32 | PHI:10956 | phoQ | *S. maltophilia* |
| 34 | PHI:5577 | esx-3 | *M. tuberculosis* |
| 38 | PHI:12129 | bglu_2g07420 | *B. glumae* |
| 39 | PHI:6687 | gra10 | *T. gondii* |
| 41 | PHI:10500 | tapV | *R. solanacearum* |
| 43 | PHI:124144 | RvvA | *V. cholerae* |
| 44 | PHI:7118 | gtfA | *S. pneumoniae* |
| 46 | PHI:4769 | HaRxLL470b | *H. arabidopsidis* |
| 47 | PHI:4715 | crc | *P. aeruginosa* |
| 51 | PHI:6998 | BfiS | *P. aeruginosa* |
| 54 | PHI:8921 | EadM | *X. axonopodis* |
| 55 | PHI:123246 | EI219_09440 | *S. suis* |
| 56 | PHI:5258 | tfpO | *P. aeruginosa* |
| 57 | PHI:124632 | UMAG_10076 | *U. maydis* |
| 60 | PHI:3120 | PSPTO_3331 | *P. syringae* |
| 64 | PHI:3593 | MgtC | *M. marinum* |
| 67 | PHI:11519 | rv3680 | *M. tuberculosis* |
| 68 | PHI:4834 | TceSR | *B. melitensis* |
| 70 | PHI:6568 | REP34 | *F. tularensis* |
| 71 | PHI:6674 | MoTRX2 | *M. oryzae* |
| 75 | PHI:5109 | prt | *S. enterica* |
| 77 | PHI:4223 | Pde2 | *S. pneumoniae* |
| 78 | PHI:4112 | MoVELB | *M. oryzae* |
| 80 | PHI:3115 | PSPTO_5633 | *P. syringae* |
| 82 | PHI:4633 | dgcB | *B. glumae* |
| 84 | PHI:10428 | vreR | *P. aeruginosa* |

**Total: 38**

### 🔴 Genuine model error (model prediction clearly wrong)

| # | PHI ID | Gene | Organism |
|---|--------|------|----------|
| 8 | PHI:123702 | dgkA | *P. aeruginosa* |
| 11 | PHI:1555 | GzMyb019 | *F. graminearum* |
| 17 | PHI:125077 | g2572 | *A. alternata* |
| 28 | PHI:9496 | yeaB | *S. enterica* |
| 30 | PHI:8915 | FgVPS32 | *F. graminearum* |
| 35 | PHI:11868 | otsA | *A. baumannii* |
| 36 | PHI:123650 | malM | *E. coli* |
| 37 | PHI:123977 | lphD | *L. pneumophila* |
| 40 | PHI:11231 | SAUSA300_0964 | *S. aureus* |
| 45 | PHI:124082 | FliY | *A. pleuropneumoniae* |
| 50 | PHI:3725 | PhoPQ | *S. enterica* |
| 52 | PHI:12224 | MoPtep1 | *M. oryzae* |
| 59 | PHI:4960 | rsmI | *S. aureus* |
| 62 | PHI:11210 | cda7 | *U. maydis* |
| 65 | PHI:4921 | flmQ | *B. cenocepacia* |
| 69 | PHI:11554 | A1479 | *B. melitensis* |
| 72 | PHI:10789 | BAB1_0270 | *B. abortus* |
| 76 | PHI:7478 | FepB | *K. pneumoniae* |
| 79 | PHI:6097 | hns | *K. pneumoniae* |
| 81 | PHI:1683 | GzRad001 | *F. graminearum* |
| 83 | PHI:7298 | PhzG1 | *P. aeruginosa* |
| 85 | PHI:3417 | Ohmm | *B. bassiana* |

**Total: 22**

---

## Summary Statistics

| Category | Count | Percentage |
|----------|-------|------------|
| 🟢 PHI-base annotation error | 20 | 23.5% |
| 🟢 Dual-function protein | 5 | 5.9% |
| 🟡 Mixed evidence | 38 | 44.7% |
| 🔴 Model error | 22 | 25.9% |
| **Total** | **85** | **100%** |

---

## Key Findings

**Nearly a quarter of all errors reflect PHI-base annotation problems rather than model failures.** Twenty of 85 misclassifications (23.5%) are cases where the model's prediction is more consistent with the literature than the PHI-base label. The most prominent patterns include ABC transporters mislabelled as "Kinase / Signalling" (potA, potC, MGA_0220, rfbE), T6SS structural components labelled as "Effector" (tssK-5, tssF-5), siderophore transporters labelled as "Secondary metabolite / Biosynthesis" (FepA), and proteins with clear transcription factor function mislabelled in other categories (flbC, ccpE, rsmAXoo, RPK1).

**Five cases represent genuine dual-function proteins** where both the PHI-base label and the model prediction capture valid aspects of the protein's biology. The recurring pattern of secretion system structural components that also function as effectors (VgrG, LcrV) and protease-effectors (PrtA) is consistent with the previous high-confidence analysis.

**The mixed evidence category is the largest (44.7%)**, reflecting the genuine biological ambiguity in assigning proteins to discrete functional classes. The most common pattern is the Kinase/Signalling ↔ TF/Regulator confusion, driven by two-component system proteins that bridge both categories, and the Effector ↔ Secretion system confusion, driven by proteins at the interface of secretion apparatus and translocated substrates.

**Model errors are concentrated in specific failure modes.** Of 22 genuine model errors, several patterns emerge: ESCRT/vesicle trafficking proteins misclassified as Kinase/Signalling (FgVPS32), subtilisin-like proteases misclassified as Kinase/Signalling (g2572), cell wall enzymes misclassified as Kinase/Signalling (flmQ, cda7, SAUSA300_0964), and several low-confidence predictions (≤0.5) that are essentially random guesses (GzRad001, PhzG1, Ohmm).

**Confidence is a reliable indicator of error type.** High-confidence errors (>0.95) are disproportionately PHI-base annotation errors, while low-confidence errors (<0.6) are more likely to be genuine model errors. This supports using model confidence as a quality filter in production deployment.
