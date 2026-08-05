#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    ListFlowable, ListItem, KeepTogether, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

AUTHOR = "Rabi Sah"

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(name="DocTitle", fontSize=20, leading=24, textColor=colors.HexColor("#1a2b4c"),
                           fontName="Helvetica-Bold", spaceAfter=6))
styles.add(ParagraphStyle(name="DocSubtitle", fontSize=11, leading=14, textColor=colors.HexColor("#555555"),
                           fontName="Helvetica", spaceAfter=16))
styles.add(ParagraphStyle(name="PhaseLabel", fontSize=10, leading=12, textColor=colors.HexColor("#1a2b4c"),
                           fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="PhaseTitle", fontSize=17, leading=21, textColor=colors.white,
                           fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="PhaseMeta", fontSize=9.5, leading=12, textColor=colors.white,
                           fontName="Helvetica"))
styles.add(ParagraphStyle(name="H2", fontSize=12.5, leading=16, textColor=colors.HexColor("#1a2b4c"),
                           fontName="Helvetica-Bold", spaceBefore=12, spaceAfter=6))
styles.add(ParagraphStyle(name="Body", fontSize=9.7, leading=13.5, fontName="Helvetica",
                           textColor=colors.HexColor("#222222"), spaceAfter=4))
styles.add(ParagraphStyle(name="BodyItalic", fontSize=9.7, leading=13.5, fontName="Helvetica-Oblique",
                           textColor=colors.HexColor("#333333"), spaceAfter=8))
styles.add(ParagraphStyle(name="Bullet", fontSize=9.5, leading=13, fontName="Helvetica",
                           textColor=colors.HexColor("#222222")))
styles.add(ParagraphStyle(name="TableHeadCell", fontSize=9, leading=11, fontName="Helvetica-Bold",
                           textColor=colors.white))
styles.add(ParagraphStyle(name="TableCell", fontSize=8.7, leading=11.5, fontName="Helvetica",
                           textColor=colors.HexColor("#222222")))
styles.add(ParagraphStyle(name="TableCellBold", fontSize=8.7, leading=11.5, fontName="Helvetica-Bold",
                           textColor=colors.HexColor("#1a2b4c")))
styles.add(ParagraphStyle(name="MetricItem", fontSize=9.5, leading=13, fontName="Helvetica",
                           textColor=colors.HexColor("#1a2b4c")))
styles.add(ParagraphStyle(name="SubNote", fontSize=9, leading=12.5, fontName="Helvetica",
                           textColor=colors.HexColor("#333333"), spaceAfter=6))

PHASE_BAR_COLOR = colors.HexColor("#2b3a67")
TABLE_HEAD_COLOR = colors.HexColor("#3d4f8c")
TABLE_ALT_COLOR = colors.HexColor("#eef0f8")

def phase_banner(label, title, months):
    data = [[Paragraph(label, styles["PhaseMeta"]),
             Paragraph(f"<b>{title}</b>", styles["PhaseTitle"]),
             Paragraph(months, styles["PhaseMeta"])]]
    t = Table(data, colWidths=[1.3*inch, 4.6*inch, 1.6*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PHASE_BAR_COLOR),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("ALIGN", (2, 0), (2, 0), "RIGHT"),
    ]))
    return t

def h2(text):
    return Paragraph(text, styles["H2"])

def body(text):
    return Paragraph(text, styles["Body"])

def italic(text):
    return Paragraph(text, styles["BodyItalic"])

def bullets(items):
    flow = [ListItem(Paragraph(i, styles["Bullet"]), leftIndent=10, spaceAfter=3) for i in items]
    return ListFlowable(flow, bulletType="bullet", start="•", leftIndent=14)

def tools_table(rows, col_widths=(2.1*inch, 5.4*inch)):
    data = [[Paragraph("Tool / Library", styles["TableHeadCell"]), Paragraph("Purpose", styles["TableHeadCell"])]]
    for tool, purpose in rows:
        data.append([Paragraph(tool, styles["TableCellBold"]), Paragraph(purpose, styles["TableCell"])])
    t = Table(data, colWidths=list(col_widths), repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEAD_COLOR),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), TABLE_ALT_COLOR))
    t.setStyle(TableStyle(style))
    return t

def subhead(text):
    return Paragraph(f"<b>{text}</b>", ParagraphStyle(name="subhead_tmp", parent=styles["Body"],
                                                        fontSize=10, textColor=colors.HexColor("#3d4f8c"),
                                                        spaceBefore=8, spaceAfter=4))

def metrics_block(items):
    flow = []
    for i in items:
        flow.append(Paragraph(f"\u2713 {i}", styles["MetricItem"]))
        flow.append(Spacer(1, 3))
    box = Table([[flow]], colWidths=[7.5*inch])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#eef6ee")),
        ("BOX", (0, 0), (-1, -1), 0.75, colors.HexColor("#8fbf8f")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return box

def why_box(text):
    t = Table([[Paragraph(f"<b>Why This Phase Matters</b><br/>{text}", styles["Body"])]], colWidths=[7.5*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f4f5fb")),
        ("BOX", (0, 0), (-1, -1), 0.75, colors.HexColor("#b9c0e0")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t

story = []

# ---------------- COVER / PAGE 1 ----------------
story.append(Paragraph("ML/AI Roadmap — Ultimate + NLP & CV Deep Dive 2026", styles["DocTitle"]))
story.append(Paragraph("Profile: Basic Python • 3–4 hrs/day • Goal: ML/AI Engineer", styles["DocSubtitle"]))
story.append(Paragraph("Prepared by Rabi Sah", ParagraphStyle(name="prep1", parent=styles["Body"], fontSize=10,
                                                                textColor=colors.HexColor("#3d4f8c"),
                                                                fontName="Helvetica-Bold", spaceAfter=14)))
story.append(h2("Complete Roadmap — 12 Phases"))

overview_rows = [
    ("Phase", "Months", "Focus", "Key Deliverables"),
    ("0 ★", "Wks 1–2", "SQL & Data Engineering", "SQL project, ETL pipeline notebook"),
    ("1", "1–2", "Python & Math", "2 mini-projects, GitHub setup"),
    ("2", "3–5", "Core ML + Tabular + Annotation", "5+ ML projects, feature store demo"),
    ("3", "6–8", "Deep Learning + GNNs", "5+ DL projects, GNN fraud demo"),
    ("3.5 ▲", "8–9", "NLP Deep Dive", "Nepali NER, multilingual models, NLP API"),
    ("3.6 ■", "9–10", "Computer Vision Deep Dive", "YOLO custom detector, OCR, SAM, tracking"),
    ("4 ◆", "10–13", "LLMs & GenAI", "RAG, Nepali NLP, diffusion, voice, multimodal"),
    ("4.2 ◆", "13", "Prompt Engineering & GenAI Patterns", "Prompt library, DSPy, 8 patterns"),
    ("4.5 ★◆", "13–14", "Eval, Safety & Responsible AI", "Eval pipeline, red-team, fairness audit"),
    ("5 ◆", "14–16", "MLOps & Production", "End-to-end pipeline, streaming LLM, LiteLLM"),
    ("5.5 ★◆", "16–17", "Inference Optimization", "Quantized serving, prompt caching, batch API"),
    ("5.8 ★◆", "17", "ML System Design", "9-step framework, 5 ML + 3 GenAI designs"),
    ("6 ★◆", "17+", "Job Prep & Career Launch", "Job offer, GenAI portfolio, blog"),
]
data = [[Paragraph(f"<b>{c}</b>", styles["TableHeadCell"]) for c in overview_rows[0]]]
for row in overview_rows[1:]:
    data.append([Paragraph(row[0], styles["TableCellBold"]), Paragraph(row[1], styles["TableCell"]),
                 Paragraph(row[2], styles["TableCell"]), Paragraph(row[3], styles["TableCell"])])
t = Table(data, colWidths=[0.9*inch, 0.8*inch, 2.6*inch, 3.2*inch], repeatRows=1)
tstyle = [
    ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEAD_COLOR),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]
for i in range(1, len(data)):
    if i % 2 == 0:
        tstyle.append(("BACKGROUND", (0, i), (-1, i), TABLE_ALT_COLOR))
t.setStyle(TableStyle(tstyle))
story.append(t)
story.append(Spacer(1, 10))
story.append(Paragraph(
    "▲ NLP Deep Dive (Phase 3.5) and ■ CV Deep Dive (Phase 3.6) are NEW phases added in this edition. "
    "They sit between Phase 3 and Phase 4 and provide specialist depth that the original roadmap covered "
    "only at surface level.", styles["SubNote"]))

story.append(PageBreak())

# ---------------- PHASE 0 ----------------
story.append(phase_banner("★ NEW Phase 0", "SQL & Data Engineering Foundations", "Weeks 1–2 | Do this FIRST"))
story.append(Spacer(1, 10))
story.append(why_box("Almost every ML job lists SQL. You will fail screening tests without it."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "SQL: SELECT, WHERE, GROUP BY, HAVING, window functions, CTEs, JOINs (INNER/LEFT/RIGHT/FULL)",
    "ETL vs ELT pipeline patterns — understand the structural difference",
    "Data formats: Parquet, JSON Lines, Avro — why Parquet beats CSV for ML",
    "Apache Spark / PySpark — DataFrames, lazy evaluation, partitions",
    "Data quality: null handling, schema validation, duplicate detection, data contracts",
]))
story.append(h2("Tools & Libraries"))
story.append(subhead("Databases"))
story.append(tools_table([
    ("SQLite", "Free zero-config local DB — perfect for SQL learning"),
    ("PostgreSQL", "Production-grade relational DB — advanced queries and indexing"),
    ("Google BigQuery (free tier)", "Cloud SQL used at large companies"),
]))
story.append(subhead("Python Libraries"))
story.append(tools_table([
    ("pandas", "DataFrames, cleaning, reshaping"),
    ("pyarrow / fastparquet", "Read/write Parquet efficiently"),
    ("sqlalchemy", "Python ORM — connect to SQLite/PostgreSQL"),
]))
story.append(subhead("Pipeline"))
story.append(tools_table([
    ("PySpark", "Distributed data processing"),
    ("dbt", "SQL into a versioned pipeline"),
]))
story.append(subhead("BI Tools"))
story.append(tools_table([
    ("DBeaver", "Free GUI for querying local databases"),
    ("Mode Analytics", "Practice SQL in BI environment"),
]))
story.append(h2("Projects"))
story.append(bullets([
    "Week 1 — SQL: Load Titanic/Netflix into SQLite. Write 15+ queries covering all clause types.",
    "Week 2 — Pipeline: Python ETL — API pull → Pandas clean → Parquet → SQLite → query results.",
]))
story.append(h2("Resources"))
story.append(bullets([
    "SQLZoo (sqlzoo.net) — free, interactive",
    "Mode SQL Tutorial — free, practical",
    "Khan Academy SQL — beginner-friendly",
    "Learning PySpark by Tomasz Drabas (Ch 1–3)",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "Can write complex SQL with JOINs and window functions confidently",
    "Understand ETL pipeline structure and key data formats",
    "Completed 1 SQL project on GitHub with 15+ queries",
    "Know what Parquet is and why it matters over CSV",
]))
story.append(PageBreak())

# ---------------- PHASE 1 ----------------
story.append(phase_banner("Phase 1", "Python & Math Foundations", "Months 1–2"))
story.append(Spacer(1, 10))
story.append(why_box("Master Python fundamentals and essential mathematics. Every phase builds directly on these foundations."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "OOP — classes, inheritance, polymorphism, magic methods",
    "File I/O — CSV, JSON, Parquet; pathlib; context managers",
    "Advanced Python — comprehensions, generators, decorators, error handling",
    "Linear Algebra — vectors, matrices, dot products, eigenvalues (conceptual)",
    "Probability & Statistics — distributions, mean/variance, Bayes theorem",
    "Calculus — derivatives, partial derivatives, chain rule",
]))
story.append(h2("Tools & Libraries"))
story.append(subhead("Core Libraries"))
story.append(tools_table([
    ("NumPy", "Arrays, vectorization, broadcasting"),
    ("Pandas", "DataFrames, cleaning, groupby"),
    ("Matplotlib", "Line, scatter, bar, subplots"),
    ("Seaborn", "Statistical visualization"),
]))
story.append(subhead("Environment"))
story.append(tools_table([
    ("VS Code", "Primary editor — Python + Jupyter extension"),
    ("Jupyter Notebook", "Interactive coding — EDA and visualization"),
    ("Google Colab", "Free cloud Jupyter — GPU access later"),
]))
story.append(subhead("Version Control"))
story.append(tools_table([
    ("Git", "Track changes — learn Day 1"),
    ("GitHub", "Portfolio hosting — every project goes here"),
]))
story.append(subhead("Math"))
story.append(tools_table([
    ("SciPy", "Scientific computing — stats, LA, optimization"),
    ("SymPy", "Symbolic math for calculus concepts"),
]))
story.append(h2("Projects"))
story.append(bullets([
    "Weeks 1–2: Personal expense tracker (OOP) — JSON save/load",
    "Weeks 3–4: Matrix calculator (NumPy) — add/multiply/transpose",
    "Weeks 5–6: Titanic Survival Analysis — EDA, cleaning, visualizations",
    "Weeks 7–8: House Price Data Explorer — correlations, 5+ chart types",
]))
story.append(h2("Resources"))
story.append(bullets([
    "Kaggle Learn — Python, Pandas, Data Viz (all free)",
    "freeCodeCamp Python (YouTube) — Beginners + Intermediate",
    "Khan Academy — Linear Algebra, Statistics, Calculus",
    "StatQuest — statistics visually | 3Blue1Brown — Essence of Linear Algebra",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "Can write classes and use inheritance confidently",
    "Comfortable with Pandas DataFrames and data cleaning",
    "Completed 2 end-to-end mini projects on GitHub with READMEs",
    "★ Started writing plain-English summaries of your work",
]))
story.append(PageBreak())

# ---------------- PHASE 2 ----------------
story.append(phase_banner("Phase 2", "Core ML + Tabular Data Mastery + Data Annotation", "Months 3–5"))
story.append(Spacer(1, 10))
story.append(why_box("Master ML workflow, all classic algorithms, tabular data production skills, and data annotation — "
                      "the phase that makes you hireable for junior ML roles."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "Supervised/Unsupervised, Train/Val/Test, Cross-Validation, Bias-Variance, Regularization",
    "Regression: Linear, Polynomial, Ridge, Lasso, ElasticNet",
    "Classification: Logistic Regression, KNN, Decision Trees, Random Forest, SVM, Naive Bayes, XGBoost",
    "Evaluation: MAE, MSE, RMSE, R², Accuracy, Precision, Recall, F1, ROC-AUC",
    "★ EDA as a structured skill — memorize checklist, narrate findings out loud",
    "★ Tabular Data Mastery — feature stores, target encoding, time-series CV",
    "★ Data Annotation — Label Studio, Snorkel weak supervision, active learning",
]))
story.append(h2("Tools & Libraries"))
story.append(subhead("Core ML"))
story.append(tools_table([
    ("scikit-learn", "All classic algorithms, pipelines, CV, metrics"),
    ("XGBoost", "Gradient boosting — Kaggle staple"),
    ("LightGBM", "Fast boosting for large datasets"),
    ("CatBoost", "Handles categoricals natively"),
    ("imbalanced-learn", "SMOTE + techniques for imbalanced data"),
]))
story.append(subhead("Tabular Mastery ★"))
story.append(tools_table([
    ("Feast", "Open-source feature store — offline/online split"),
    ("category_encoders", "Target encoding, WoE, leave-one-out"),
    ("optuna", "Hyperparameter optimization — replaces GridSearchCV"),
    ("feature-engine", "sklearn-compatible feature engineering transformers"),
]))
story.append(subhead("Annotation ★"))
story.append(tools_table([
    ("Label Studio", "Open-source annotation — text, image, audio, NER, classification"),
    ("Snorkel", "Programmatic labeling — write labeling functions"),
    ("cleanlab", "Find and fix label errors automatically"),
]))
story.append(subhead("Explainability"))
story.append(tools_table([
    ("SHAP", "Explain any model — beeswarm, waterfall, force plots"),
    ("LIME", "Local model-agnostic explanations"),
    ("ydata-profiling", "One-line automated EDA report generation"),
]))
story.append(h2("Projects"))
story.append(bullets([
    "Month 3: Email Spam Classifier + Customer Churn Prediction",
    "Month 4: House Price Prediction (Kaggle) + Time Series Forecasting with purged CV",
    "Month 5: Medical Diagnosis Classifier (SMOTE, SHAP) + First Kaggle Competition",
    "★ Bonus: Feature store demo with Feast + annotate 200 Nepali tweets in Label Studio",
]))
story.append(h2("Resources"))
story.append(bullets([
    "Andrew Ng ML Specialization (Coursera, audit free) — most important resource",
    "Google ML Crash Course (free) | Kaggle Learn Intermediate ML",
    "'Hands-On Machine Learning' by Aurélien Géron",
    "Snorkel documentation (snorkel.ai) | Label Studio documentation",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "Completed Andrew Ng ML Specialization",
    "Can explain 8+ ML algorithms and their trade-offs clearly",
    "★ Can perform structured EDA and narrate findings clearly",
    "★ Built and registered features in Feast | Annotated real dataset in Label Studio",
]))
story.append(PageBreak())

# ---------------- PHASE 3 ----------------
story.append(phase_banner("Phase 3", "Deep Learning, Neural Networks & Graph Neural Networks", "Months 6–8"))
story.append(Spacer(1, 10))
story.append(why_box("Master PyTorch, CNNs, RNNs, GNNs, and multimodal models. This separates ML engineers from data analysts."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "MLP, activation functions, forward/backpropagation, optimizers (SGD, Adam, AdamW)",
    "CNNs — convolutions, pooling, ResNet, EfficientNet, Transfer Learning",
    "RNNs, LSTMs, GRUs — sequence modeling, BPTT, bidirectional",
    "Regularization — Dropout, Batch Norm, Layer Norm, He/Xavier initialization",
    "★ GNNs — message passing, GCN, GAT, GraphSAGE, node/link/graph tasks",
    "★ Multimodal — CLIP, LLaVA, vision-language architecture",
]))
story.append(h2("Tools & Libraries"))
story.append(subhead("DL Framework"))
story.append(tools_table([
    ("PyTorch", "Primary — custom models, autograd, training loops"),
    ("torchvision", "ResNet, EfficientNet, datasets, transforms"),
    ("TensorBoard", "Visualize training curves in real time"),
    ("Weights & Biases", "Experiment tracking, sweeps (free tier)"),
]))
story.append(subhead("GNNs ★"))
story.append(tools_table([
    ("PyTorch Geometric (PyG)", "GCN, GAT, GraphSAGE, GIN, graph data loaders"),
    ("DGL (Deep Graph Library)", "Alternative GNN — excellent docs, PyTorch backend"),
    ("NetworkX", "Graph analysis and visualization in Python"),
    ("OGB (Open Graph Benchmark)", "Standardized GNN benchmarks"),
]))
story.append(subhead("Multimodal ★"))
story.append(tools_table([
    ("CLIP (openai/clip)", "Vision-language embedding model"),
    ("LLaVA / PaliGemma", "Open-source VLMs on HuggingFace"),
    ("Albumentations", "Fast rich image augmentation"),
    ("Gradio", "Build interactive ML demos instantly"),
]))
story.append(h2("Projects"))
story.append(bullets([
    "Month 6: MNIST from scratch (manual backprop) + Binary Classification NN",
    "Month 7: CIFAR-10 CNN (Grad-CAM + Gradio) + Transfer Learning (ResNet50)",
    "Month 8: LSTM Time Series + Sentiment + Character-level Language Model",
    "★ GNN: Node classification on Cora (GCN vs GAT) + Fraud detection with PyG",
    "★ Multimodal: Image captioning or VQA demo using LLaVA",
]))
story.append(h2("Resources"))
story.append(bullets([
    "Karpathy 'Zero to Hero' (YouTube, FREE — ESSENTIAL, ~20hrs)",
    "Fast.ai Practical Deep Learning (free) | DeepLearning.AI Specialization (audit free)",
    "Stanford CS224W — ML with Graphs (free YouTube) | PyG tutorials",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "Completed Karpathy's Zero to Hero series",
    "Built NN from scratch — truly understand backpropagation",
    "★ Built GNN — can explain message passing, GCN vs GAT vs GraphSAGE",
    "★ Built multimodal (vision + language) demo",
]))
story.append(PageBreak())

# ---------------- PHASE 3.5 NLP ----------------
story.append(phase_banner("▲ NEW Phase 3.5", "NLP Deep Dive — Classical to Multilingual to Nepali", "Months 8–9 | NEW PHASE"))
story.append(Spacer(1, 10))
story.append(why_box(
    "The original roadmap treats NLP as a subset of LLMs — which misses the classical foundations that ML "
    "interviews still test. This phase fills that gap with a complete NLP track: from tokenization theory and "
    "word embeddings to multilingual transformers and Nepali-specific tools. Your Nepali NLP project will be "
    "dramatically stronger with this foundation — you will understand WHY XLM-R works for Nepali and HOW to "
    "diagnose failures when it doesn't."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "Classical NLP pipeline — tokenization, stemming, lemmatization, POS tagging, NER, dependency parsing",
    "Text preprocessing mastery — cleaning, normalization, Unicode handling, language detection",
    "Word embeddings — Word2Vec (skip-gram, CBOW), GloVe (global co-occurrence), FastText (subword)",
    "Advanced tasks — NER, relation extraction, coreference resolution, extractive QA, summarization",
    "Multilingual NLP — mBERT, XLM-R, IndicBERT for low-resource languages",
    "Nepali NLP specialization — IndicNLP, Stanza Nepali, CC-100, Leipzig Nepali corpora",
    "NLP evaluation — BLEU, ROUGE, BERTScore, F1 for NER, exact match for QA",
    "NLP production — spaCy pipelines, ONNX export, FastAPI NLP APIs",
]))
story.append(h2("Core NLP Concepts to Master"))
story.append(bullets([
    "Tokenization strategies: whitespace vs WordPiece vs BPE vs SentencePiece — when each is best",
    "Stemming (Porter, Snowball) vs Lemmatization — morphological analysis for Nepali (agglutinative language)",
    "POS tagging: rule-based vs statistical vs neural — spaCy uses CNN + transition-based parser",
    "Named Entity Recognition: BIO/BIOES tagging scheme, CRF layer, transformer fine-tuning",
    "Word2Vec: skip-gram (predict context from word) vs CBOW (predict word from context), negative sampling",
    "FastText advantage: character n-grams handle OOV — crucial for Nepali morphology and code-mixed text",
    "XLM-R vs mBERT: XLM-R uses more data, larger vocabulary, better cross-lingual transfer for low-resource",
    "Subword tokenization and Nepali: SentencePiece handles Devanagari Unicode without manual segmentation",
    "Transliteration: Devanagari script to Roman (useful for code-mixed Romanized Nepali on social media)",
    "Data augmentation for low-resource NLP: back-translation, synonym replacement, random deletion",
]))
story.append(PageBreak())

story.append(h2("Tools & Libraries — Complete NLP Stack"))
story.append(subhead("Classical NLP & Text Processing"))
story.append(tools_table([
    ("spaCy", "Industrial-strength NLP — tokenization, POS, NER, dependency parsing, pipelines"),
    ("NLTK", "Natural Language Toolkit — stemming, lemmatization, corpora, WordNet, CFG parsing"),
    ("Gensim", "Topic modeling (LDA, LSA), Word2Vec, FastText training from scratch"),
    ("regex (re)", "Python's regex module — essential for text cleaning, pattern extraction"),
    ("ftfy", "Fix mangled Unicode text — critical for Nepali and multilingual data cleaning"),
    ("langdetect / langid", "Language detection — identify language before processing multilingual corpora"),
    ("chardet", "Character encoding detection — handle UTF-8/ASCII/Latin mismatch in scraped data"),
]))
story.append(subhead("Word Embeddings"))
story.append(tools_table([
    ("Gensim Word2Vec", "Train skip-gram / CBOW word embeddings from scratch on your own corpus"),
    ("GloVe (pre-trained)", "Global Vectors — download pre-trained 50/100/300d embeddings for English"),
    ("FastText (Facebook)", "Subword embeddings — handles OOV words, excellent for morphologically rich languages like Nepali"),
    ("fasttext (Python lib)", "Train FastText embeddings locally — best choice for Nepali NLP word vectors"),
    ("Magnitude", "Fast, unified embedding loading — supports Word2Vec, GloVe, FastText formats"),
]))
story.append(subhead("Multilingual & Low-Resource NLP"))
story.append(tools_table([
    ("mBERT (multilingual BERT)", "Pre-trained on 104 languages including Nepali — fine-tune for NLP tasks"),
    ("XLM-RoBERTa (XLM-R)", "Better than mBERT for low-resource languages — HuggingFace transformers"),
    ("IndicBERT / IndicNLP", "BERT trained on 12 Indic languages — strong Nepali representation"),
    ("IndicNLP Library", "Tokenization, transliteration, and normalization for Indic languages incl. Nepali"),
    ("Stanza (Stanford NLP)", "Multilingual NLP pipeline — 70+ languages, includes Nepali POS + NER"),
    ("Polyglot", "Multilingual NLP — transliteration, named entity, sentiment for 130+ languages"),
    ("Aksharamukha", "Script converter — Devanagari (Nepali) to/from Latin, Romanized Nepali handling"),
]))
story.append(subhead("Advanced NLP Tasks"))
story.append(tools_table([
    ("spaCy + spaCy-transformers", "NER, relation extraction, text classification with transformer backbone"),
    ("Flair", "State-of-the-art NER and sequence labeling — character-level language model embeddings"),
    ("AllenNLP", "Research-grade NLP — coreference resolution, SRL, reading comprehension"),
    ("Haystack (deepset)", "End-to-end NLP pipelines — QA, summarization, NER at production scale"),
    ("sumy / bert-extractive-summarizer", "Extractive summarization — pick key sentences from long documents"),
    ("TextBlob", "Lightweight NLP — sentiment analysis, noun phrase extraction, quick prototyping"),
]))
story.append(PageBreak())

story.append(subhead("NLP Evaluation & Datasets"))
story.append(tools_table([
    ("evaluate (HuggingFace)", "Compute BLEU, ROUGE, BERTScore, METEOR, WER metrics — one import"),
    ("sacrebleu", "Standardized BLEU score — industry standard for translation evaluation"),
    ("datasets (HuggingFace)", "Load NLP benchmarks — GLUE, SuperGLUE, SQuAD, CC-100 Nepali subset"),
    ("Leipzig Corpora", "Nepali news + web corpora — best free Nepali text dataset"),
    ("CC-100 Nepali", "CommonCrawl Nepali subset — 270MB of Nepali web text for pretraining"),
    ("IndicGLUE", "Benchmark for Indic language NLP models — includes Nepali tasks"),
]))
story.append(subhead("NLP Production & Deployment"))
story.append(tools_table([
    ("FastAPI + spaCy", "Serve NLP pipelines as REST APIs — NER, classification, similarity endpoints"),
    ("spaCy projects", "Version-controlled NLP pipelines — config-driven, reproducible training"),
    ("Prodigy (Explosion.ai)", "Active learning annotation tool from spaCy team — fast NLP labeling"),
    ("Weights & Biases", "Track NLP experiment metrics — loss, F1, BLEU curves per epoch"),
    ("ONNX Runtime", "Export spaCy / HuggingFace NLP models to ONNX for fast CPU inference"),
]))
story.append(h2("Hands-On Projects"))
story.append(bullets([
    "Nepali NER System — train spaCy + XLM-R NER on manually annotated Nepali text (use Label Studio from Phase 2)",
    "Multilingual Sentiment Analyzer — fine-tune XLM-R on Nepali Twitter data (positive/negative/neutral)",
    "Nepali Text Preprocessor Library — publish to PyPI: tokenizer, normalizer, Devanagari cleaner",
    "Nepali-English Word Embeddings — train FastText on CC-100 Nepali + Leipzig corpora, publish to HuggingFace",
    "Document Information Extractor — spaCy NER pipeline for extracting entities from Nepali news articles",
    "Coreference Resolution Demo — AllenNLP coreference on English + evaluate on Nepali using XLM-R",
    "NLP API — FastAPI serving spaCy Nepali pipeline: /tokenize, /ner, /similarity, /language-detect endpoints",
]))
story.append(h2("Nepali NLP Data Sources"))
story.append(bullets([
    "CC-100 Nepali subset — CommonCrawl Nepali text (~270MB) — use for FastText pretraining",
    "Leipzig Corpora (Nepali) — news + web text — download from wortschatz.uni-leipzig.de",
    "IndicGLUE Nepali — benchmark tasks for Nepali NLP model evaluation",
    "Nepali NLP GitHub (oknlp/nepali-nlp) — community resources, datasets, models",
    "AI4Bharat datasets — Nepali ASR, NER, translation parallel corpora",
    "FLORES-200 — multilingual benchmark including Nepali — test your models here",
]))
story.append(h2("Study Resources"))
story.append(bullets([
    "spaCy Course (course.spacy.io) — free, interactive, covers spaCy v3 and transformer integration",
    "Stanford CS224N (free, YouTube) — NLP with Deep Learning — best free NLP course available",
    "HuggingFace NLP Course (huggingface.co/learn) — free, covers transformers for all NLP tasks",
    "IndicNLP documentation (indicnlp.ai4bharat.org) — tools for Nepali and other Indic languages",
    "Stanza documentation (stanfordnlp.github.io/stanza) — Nepali NLP pipeline",
    "'Speech and Language Processing' by Jurafsky & Martin (free PDF) — comprehensive NLP theory",
    "Lena Voita's NLP Course (lena-voita.github.io) — exceptional visual explanations of NLP concepts",
    "Leipzig Corpora Collection (wortschatz.uni-leipzig.de) — free Nepali text corpora",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "Built a complete Nepali NLP preprocessing pipeline (tokenizer + normalizer + NER)",
    "Trained FastText embeddings on Nepali text and evaluated on word similarity tasks",
    "Fine-tuned XLM-R or IndicBERT for at least one Nepali NLP task (NER or sentiment)",
    "Can explain Word2Vec skip-gram, GloVe co-occurrence matrix, and FastText subwords clearly",
    "Deployed an NLP API with FastAPI serving spaCy + transformer model endpoints",
    "Published Nepali NLP work to HuggingFace Hub (model or dataset) — visible to the world",
    "Can discuss low-resource NLP challenges and mitigation strategies in an interview",
]))
story.append(PageBreak())

# ---------------- PHASE 3.6 CV ----------------
story.append(phase_banner("■ NEW Phase 3.6", "Computer Vision Deep Dive — Classical to Multimodal to Production", "Months 9–10 | NEW PHASE"))
story.append(Spacer(1, 10))
story.append(why_box(
    "Phase 3 covers CNNs and transfer learning — but that is table stakes. This phase adds the full CV "
    "engineering stack used in industry: YOLO-based detection pipelines, SAM for zero-shot segmentation, "
    "OCR for Devanagari Nepali text (your unique differentiator), multi-object tracking for video, depth "
    "estimation, and production CV deployment with ONNX and TensorRT. Companies with active CV teams look "
    "for exactly this depth — this phase makes you credible in those interviews."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "Classical CV — image representation, color spaces (RGB/HSV/LAB), convolution filters, edge detection",
    "Feature detection — SIFT, ORB, HOG, Harris corner — understand before deep learning",
    "Object detection — YOLO family (v5/v8/v11), Faster R-CNN, DETR — train on custom datasets",
    "Image segmentation — semantic (SegFormer), instance (Mask R-CNN), panoptic, SAM zero-shot",
    "Pose estimation — MediaPipe (real-time), ViTPose (SOTA), multi-person tracking",
    "OCR pipeline — Tesseract, EasyOCR, PaddleOCR, TrOCR, Donut for document understanding",
    "3D vision — monocular depth (MiDaS, Depth Anything), point cloud basics, NeRF concepts",
    "Video understanding — optical flow, action recognition, multi-object tracking",
    "CV production — ONNX export, TensorRT optimization, DeepStream pipeline, Triton serving",
]))
story.append(h2("Core CV Concepts to Master"))
story.append(bullets([
    "Image representation: pixels, channels, color spaces — RGB vs HSV vs LAB and when to use each",
    "Convolution filters: Sobel (edges), Gaussian (blur), Laplacian (sharpening) — foundation of CNNs",
    "HOG features: Histogram of Oriented Gradients — backbone of pre-deep-learning pedestrian detection",
    "SIFT vs ORB: SIFT scale/rotation invariant (patented), ORB faster open-source alternative",
    "Anchor boxes in YOLO/Faster R-CNN: predefined aspect ratios at each grid cell for multi-scale detection",
    "IoU (Intersection over Union): detection metric — NMS uses IoU to suppress duplicate boxes",
    "mAP (mean Average Precision): standard detection metric — mAP@0.5 and mAP@0.5:0.95",
    "Semantic vs Instance vs Panoptic segmentation: scene-level vs object-level vs unified",
    "SAM (Segment Anything): promptable segmentation — ViT image encoder + prompt encoder + mask decoder",
    "Optical flow: dense (RAFT) vs sparse (Lucas-Kanade) — pixel motion estimation between frames",
    "NeRF (Neural Radiance Fields): scene represented as MLP — novel view synthesis from sparse images",
    "Monocular depth estimation: single image → relative depth — MiDaS uses encoder-decoder with DPT head",
    "Transfer learning strategy for CV: ImageNet pre-trained → freeze backbone → fine-tune head → unfreeze top layers",
    "Data augmentation for CV: horizontal flip, random crop, mosaic (YOLO), MixUp, CutMix",
]))
story.append(PageBreak())

story.append(h2("Tools & Libraries — Complete CV Stack"))
story.append(subhead("Classical Computer Vision"))
story.append(tools_table([
    ("OpenCV (cv2)", "The essential CV library — image I/O, color spaces, filters, morphology, feature detection"),
    ("Pillow (PIL)", "Python image processing — resize, crop, rotate, format conversion, basic filters"),
    ("scikit-image", "Scientific image processing — segmentation, feature extraction, morphology"),
    ("imageio", "Read/write images and video frames — supports 100+ formats including medical imaging"),
    ("albumentations", "Fast, rich image augmentation — the standard for training data pipelines"),
]))
story.append(subhead("Object Detection"))
story.append(tools_table([
    ("Ultralytics (YOLOv8 / YOLO11)", "State-of-the-art real-time detection — detect, segment, pose, track in one library"),
    ("YOLOv5 (Ultralytics)", "Mature, battle-tested detection — huge community, excellent export support"),
    ("Detectron2 (Facebook)", "Research-grade detection — Faster R-CNN, Mask R-CNN, DETR, panoptic"),
    ("MMDetection (OpenMMLab)", "Modular detection framework — 300+ models, easy architecture swapping"),
    ("RT-DETR (Baidu)", "Real-time DETR — transformer detection without NMS, competitive with YOLOv8"),
    ("Roboflow", "Dataset management + annotation + training for detection — free tier available"),
    ("supervision", "Post-processing utilities for detection — annotations, tracking, zones — works with any model"),
]))
story.append(subhead("Image Segmentation"))
story.append(tools_table([
    ("SAM (Segment Anything, Meta)", "Zero-shot segmentation — prompt with point/box/text, segment any object"),
    ("SAM 2", "Upgraded SAM — extends to video segmentation, faster, more accurate"),
    ("MMSegmentation", "Semantic segmentation framework — DeepLabV3+, SegFormer, Swin-based models"),
    ("Mask R-CNN (Detectron2)", "Instance segmentation — separate mask per detected object instance"),
    ("SegFormer (HuggingFace)", "Transformer-based semantic segmentation — lightweight and powerful"),
    ("SEEM / SAM-HQ", "Enhanced SAM variants — better quality masks for complex scenes"),
]))
story.append(PageBreak())

story.append(subhead("Pose Estimation & Tracking"))
story.append(tools_table([
    ("MediaPipe (Google)", "Real-time pose, hand, face landmark detection — runs on CPU, great for demos"),
    ("ViTPose (HuggingFace)", "Transformer-based pose estimation — SOTA on COCO benchmark"),
    ("OpenPose (CMU)", "Multi-person pose estimation — classic approach, well-documented"),
    ("ByteTrack / StrongSORT", "Multi-object tracking — associate detections across frames (used with YOLO)"),
    ("DeepSORT", "Deep learning multi-object tracking — appearance + motion features"),
]))
story.append(subhead("OCR & Document Understanding"))
story.append(tools_table([
    ("Tesseract (pytesseract)", "Classic OCR engine — text extraction from images, supports 100+ languages"),
    ("EasyOCR", "Deep learning OCR — 80+ languages, easy setup, GPU accelerated"),
    ("PaddleOCR", "SOTA OCR from Baidu — detection + recognition + layout analysis in one pipeline"),
    ("TrOCR (HuggingFace)", "Transformer OCR — fine-tune on custom handwriting or printed text"),
    ("Donut (HuggingFace)", "Document understanding without OCR — VQA on documents, form extraction"),
    ("LayoutLMv3 (HuggingFace)", "Multimodal document understanding — combines text + layout + image features"),
]))
story.append(subhead("3D Vision & Depth Estimation"))
story.append(tools_table([
    ("MiDaS (Intel)", "Monocular depth estimation — single image → depth map, runs locally"),
    ("Depth Anything v2", "SOTA monocular depth — better generalization than MiDaS on in-the-wild images"),
    ("Open3D", "3D data processing — point clouds, mesh, visualization, registration"),
    ("PyTorch3D (Facebook)", "3D deep learning — mesh rendering, 3D convolutions, NeRF experiments"),
    ("NeRFstudio", "Modular NeRF framework — train Neural Radiance Fields on custom scenes"),
]))
story.append(PageBreak())

story.append(subhead("Video Understanding"))
story.append(tools_table([
    ("PyTorch Video (fvcore)", "Video understanding framework — action recognition, SlowFast, MViT"),
    ("VideoMAE (HuggingFace)", "Masked autoencoder for video — SOTA action recognition pre-training"),
    ("RAFT / FlowNet", "Optical flow estimation — motion between frames for action recognition"),
    ("ffmpeg-python", "Video I/O and processing — extract frames, resize, encode/decode pipelines"),
    ("decord", "Fast video decoder — read video frames directly into NumPy/PyTorch tensors"),
]))
story.append(subhead("CV in Production"))
story.append(tools_table([
    ("ONNX + ONNX Runtime", "Export PyTorch CV models to ONNX for hardware-agnostic fast inference"),
    ("TensorRT (NVIDIA)", "GPU inference optimization — up to 8x speedup for detection/segmentation models"),
    ("DeepStream (NVIDIA)", "End-to-end streaming CV pipeline — multi-camera, real-time, production grade"),
    ("Triton Inference Server", "Scalable CV model serving — dynamic batching, multiple model backends"),
    ("Gradio + cv2", "Build CV demos with webcam input — real-time inference demo in 20 lines"),
    ("Label Studio (CV mode)", "Annotation for bounding boxes, polygons, keypoints, segmentation masks"),
]))
story.append(h2("Hands-On Projects"))
story.append(bullets([
    "Custom Object Detector — train YOLOv8 on a custom dataset (200+ images, labeled in Roboflow)",
    "Instance Segmentation Demo — Mask R-CNN or SAM on custom images with Gradio UI",
    "OCR Pipeline for Nepali Documents — PaddleOCR fine-tuned on Nepali Devanagari text, FastAPI endpoint",
    "Pose Estimation App — MediaPipe real-time pose + angle measurement (fitness/sports analysis)",
    "Document Understanding System — Donut or LayoutLMv3 extracting structured data from forms",
    "Multi-Object Tracking Demo — YOLOv8 + ByteTrack tracking people/vehicles in video",
    "Depth Estimation Demo — Depth Anything v2 on uploaded images, 3D point cloud visualization (Open3D)",
    "Defect Detection System — train YOLO on industrial defect images (Kaggle datasets available)",
    "Nepali OCR — fine-tune TrOCR or PaddleOCR on Nepali handwritten text dataset",
]))
story.append(h2("CV Dataset Resources"))
story.append(bullets([
    "COCO (cocodataset.org) — 80 categories, detection + segmentation + keypoints — the standard benchmark",
    "ImageNet (image-net.org) — 1000 classes, 1.2M images — understand it even if you use pretrained models",
    "Open Images (Google) — 9M images, 600 categories, bounding boxes + segmentation",
    "Roboflow Universe (roboflow.com/universe) — 100K+ custom datasets for niche domains",
    "Kaggle CV competitions — chest X-ray, satellite imagery, document detection — great for portfolio",
    "ICDAR datasets — document understanding and OCR benchmarks — relevant for Nepali OCR work",
    "WiderFace — face detection benchmark | LFW — face verification benchmark",
]))
story.append(PageBreak())

story.append(h2("Nepali OCR — Your Unique CV Differentiator"))
story.append(body(
    "Nepali Devanagari OCR is a genuinely unsolved problem — most OCR systems perform poorly on Nepali text, "
    "especially handwritten or historical documents. Building a working Nepali OCR pipeline puts you in the "
    "top 0.1% of CV portfolios globally."))
story.append(body(
    "Approach: (1) Use PaddleOCR's multilingual Devanagari model as baseline. (2) Fine-tune TrOCR on Nepali "
    "printed text from publicly available Nepali newspapers/documents. (3) Evaluate on both printed and "
    "handwritten Nepali text. (4) Package as a HuggingFace Space demo. This project combines your NLP Phase "
    "3.5 Nepali work with CV — a true portfolio centerpiece."))
story.append(h2("Study Resources"))
story.append(bullets([
    "CS231n Stanford (free, YouTube) — Convolutional Neural Networks for Visual Recognition — ESSENTIAL",
    "Ultralytics YOLOv8 documentation (docs.ultralytics.com) — object detection, segmentation, pose",
    "OpenCV Python tutorials (docs.opencv.org) — comprehensive classical CV tutorials",
    "Roboflow Blog (blog.roboflow.com) — practical CV tutorials, dataset tips, model comparisons",
    "HuggingFace CV tasks (huggingface.co/docs/transformers/tasks) — ViT, DETR, SegFormer tutorials",
    "PyImageSearch (pyimagesearch.com) — free blog, practical OpenCV + deep learning tutorials",
    "SAM documentation (segment-anything.com) — Meta's Segment Anything model tutorials",
    "PaddleOCR documentation (github.com/PaddlePaddle/PaddleOCR) — free, multilingual OCR",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "Can implement image preprocessing pipeline in OpenCV from scratch (resize, normalize, augment)",
    "Trained YOLOv8 on a custom dataset and achieved >0.7 mAP@0.5",
    "Built a segmentation demo using SAM — zero-shot on custom images",
    "Built an OCR pipeline for Nepali Devanagari text using PaddleOCR or TrOCR",
    "Deployed a real-time CV model with Gradio demo (webcam or image upload)",
    "Can explain mAP, IoU, NMS, anchor boxes, and FPN in a CV interview",
    "Built a multi-object tracking system using YOLOv8 + ByteTrack on video",
    "Exported a CV model to ONNX and measured inference speedup",
]))
story.append(PageBreak())

# ---------------- PHASE 4 ----------------
story.append(phase_banner("◆ Phase 4", "LLMs & Generative AI ◆ GenAI Enhanced", "Months 10–13"))
story.append(Spacer(1, 10))
story.append(why_box(
    "Master Transformers, HuggingFace ecosystem, RAG, LLM fine-tuning, diffusion models, multimodal LLMs, "
    "and audio AI. Every top ML company expects LLM expertise in 2026."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "Transformer: self-attention, multi-head, positional encoding, residual connections",
    "LLM families: GPT, BERT, LLaMA, Mistral, Gemma — tokenization (BPE, WordPiece, SentencePiece)",
    "PEFT: LoRA, QLoRA, prompt tuning, adapters — fine-tune 7B on consumer hardware",
    "RAG pipeline: chunking, vector databases (ChromaDB, FAISS), embeddings, re-ranking",
    "★ Structured outputs — Instructor (Pydantic), Outlines (grammar), Ollama (local JSON mode)",
    "★ Nepali NLP fine-tune — QLoRA on Mistral-7B for translation/NER/sentiment (TOP PRIORITY)",
    "◆ Diffusion models — DDPM, DDIM, classifier-free guidance, LoRA for custom styles",
    "◆ Multimodal LLMs — GPT-4o Vision, Gemini, Claude Vision, LLaVA, Phi-3-Vision",
    "◆ Audio AI — Whisper STT, faster-whisper, Coqui TTS, Bark, ElevenLabs voice pipeline",
]))
story.append(h2("Tools & Libraries"))
story.append(subhead("HuggingFace Ecosystem"))
story.append(tools_table([
    ("transformers", "Load, fine-tune, run any LLM"),
    ("peft", "LoRA/QLoRA — LLMs on consumer GPU"),
    ("datasets", "Load/stream large datasets"),
    ("evaluate", "BLEU, ROUGE, BERTScore"),
    ("accelerate", "Distributed training + mixed precision"),
    ("trl", "SFT, RLHF, DPO loops"),
    ("Unsloth", "2x faster QLoRA with less VRAM"),
]))
story.append(subhead("RAG Stack"))
story.append(tools_table([
    ("LangChain", "Document loaders, chains, agents, memory"),
    ("LlamaIndex", "Advanced RAG, query engines"),
    ("ChromaDB", "Local vector DB"),
    ("FAISS", "Fast similarity search at scale"),
    ("Sentence-Transformers", "High-quality embeddings"),
]))
story.append(PageBreak())
story.append(subhead("GenAI ◆"))
story.append(tools_table([
    ("Diffusers (HuggingFace) ◆", "Stable Diffusion, SDXL, Flux locally"),
    ("ComfyUI ◆", "Node-based SD workflow — used in production"),
    ("Whisper (OpenAI) ◆", "STT — supports Nepali transcription"),
    ("faster-whisper ◆", "4x faster Whisper — lower memory"),
    ("ElevenLabs API ◆", "Production TTS — best quality, free tier"),
    ("Coqui TTS ◆", "Open-source TTS + voice cloning — local inference"),
]))
story.append(subhead("Deployment"))
story.append(tools_table([
    ("Gradio", "LLM chat + demo interfaces"),
    ("Streamlit", "RAG system dashboards"),
    ("HuggingFace Spaces", "Free hosting for all demos"),
    ("bitsandbytes", "INT4/INT8 quantization"),
]))
story.append(h2("Projects"))
story.append(bullets([
    "Month 10: Transformer from scratch + BERT fine-tuning for text classification",
    "Month 11: Document QA (LangChain + ChromaDB) + Multi-doc RAG with re-ranking",
    "Month 12: ★ Nepali NLP fine-tune (QLoRA on Mistral-7B) + instruction-tuned model",
    "Month 13: Multi-agent system + LLM tool use + structured JSON extraction",
    "◆ Multimodal product description generator (image → LLaVA → structured JSON)",
    "◆ Stable Diffusion + ControlNet demo for product image variations",
    "◆ Voice pipeline: Whisper STT → LLM summarize → ElevenLabs TTS reads aloud",
]))
story.append(h2("Resources"))
story.append(bullets([
    "HuggingFace LLM Course (free — ESSENTIAL) | Karpathy 'Let's Build GPT' (YouTube)",
    "'Attention Is All You Need' paper | Umar Jamil (YouTube) — Transformer from scratch",
    "◆ HuggingFace Diffusion Models Course (free) | Fast.ai Part 2 (Stable Diffusion)",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "Can explain Transformer architecture from scratch",
    "Fine-tuned ≥1 LLM (7B+ params) with QLoRA — ★ Nepali NLP project deployed",
    "Built working RAG system with vector DB and deployed Gradio demo",
    "◆ Built diffusion model demo + multimodal pipeline + voice STT→LLM→TTS pipeline",
]))
story.append(PageBreak())

# ---------------- PHASE 4.2 ----------------
story.append(phase_banner("◆ NEW Phase 4.2", "Prompt Engineering & GenAI Application Patterns ◆", "Month 13 | NEW PHASE"))
story.append(Spacer(1, 10))
story.append(why_box(
    "Prompt engineering is a real engineering discipline in 2026. Companies expect production-grade prompts "
    "and GenAI application architectures — skills most self-taught engineers entirely lack."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "◆ Core techniques — zero-shot, few-shot, chain-of-thought, self-consistency, ReAct, Tree of Thoughts",
    "◆ System prompt design — persona, constraints, output formatting, jailbreak resistance",
    "◆ Prompt templates + versioning — treat prompts like code (version control, CI/CD)",
    "◆ DSPy — programmatic prompting: auto-optimize prompts from examples, not by hand",
    "◆ Context window management — chunking, token budgeting, long-context models",
    "◆ 8 GenAI application patterns — RAG, ReAct, Map-Reduce, Self-Consistency, Extraction, etc.",
    "◆ Multimodal prompting — vision models, interleaving image+text inputs",
]))
story.append(h2("Tools & Libraries"))
story.append(subhead("Prompt Engineering ◆"))
story.append(tools_table([
    ("DSPy (Stanford) ◆", "Programmatic prompting — auto-find optimal prompt from examples"),
    ("PromptFlow (Microsoft) ◆", "End-to-end prompt pipeline dev + testing"),
    ("LangSmith ◆", "Prompt versioning, A/B testing, tracing"),
    ("Promptfoo ◆", "Automated prompt testing across models"),
    ("Instructor ◆", "Force any LLM to return valid Pydantic models"),
    ("Guidance (Microsoft) ◆", "Constrained generation — interleave prompts and code"),
    ("Helicone ◆", "LLM observability + prompt management — open source"),
]))
story.append(subhead("Testing Tools"))
story.append(tools_table([
    ("Anthropic Workbench ◆", "Test prompts visually — console.anthropic.com — free"),
    ("OpenAI Playground ◆", "Test GPT-4o with JSON mode, system prompts"),
    ("Ollama + Open WebUI ◆", "Local LLM + browser UI — test without API costs"),
]))
story.append(h2("Projects"))
story.append(bullets([
    "◆ Prompt Library: Build versioned library for 5 tasks — CoT vs few-shot vs zero-shot",
    "◆ DSPy Optimizer: Auto-optimize a classification prompt — benchmark vs hand-crafted",
    "◆ Structured Extraction: Invoice/receipt parser (Instructor + GPT-4o → Pydantic models)",
    "◆ Prompt Regression Suite: 20 test cases for Nepali NLP prompts using Promptfoo",
    "◆ Multimodal RAG: Product image + description retrieval (CLIP + text embeddings + FAISS)",
]))
story.append(h2("Resources"))
story.append(bullets([
    "◆ Anthropic Prompt Engineering Guide (docs.anthropic.com) — free, authoritative",
    "◆ OpenAI Prompt Engineering Guide (platform.openai.com) — free",
    "◆ DSPy documentation (dspy.ai) | DeepLearning.AI Prompt Engineering course (free)",
    "◆ Lilian Weng's blog — ReAct, ToT, agent prompting deep dives",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "◆ Built versioned prompt library with Promptfoo regression tests",
    "◆ Used DSPy to auto-optimize a prompt pipeline — documented improvement",
    "◆ Built structured extraction system with Instructor",
    "◆ Can design GenAI application pattern for 5 different business problems",
]))
story.append(PageBreak())

# ---------------- PHASE 4.5 ----------------
story.append(phase_banner("★◆ NEW Phase 4.5", "LLM Evaluation, Safety, Agentic AI & Responsible AI", "Months 13–14 | NEW + Enhanced"))
story.append(Spacer(1, 10))
story.append(why_box(
    "Evaluation, agentic systems, Responsible AI, and GenAI safety are the fastest-growing areas in "
    "production LLM work. All appear in every senior LLM interview in 2026."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "LLM-as-judge pattern, BLEU/ROUGE/BERTScore/G-Eval, hallucination detection",
    "Agentic AI — LangGraph, tool calling, memory, long-horizon planning",
    "★ Responsible AI — Fairlearn, AIF360, demographic parity, equalized odds",
    "◆ GenAI safety — PyRIT red-teaming, Rebuff injection defense, OWASP Top 10 for LLMs",
    "◆ Copyright in generated content, deepfake risk, PII leakage in fine-tuned models",
    "EU AI Act risk tiers — high-risk system requirements, fairness documentation",
]))
story.append(h2("Tools & Libraries"))
story.append(subhead("Evaluation"))
story.append(tools_table([
    ("DeepEval", "Pytest-style LLM testing — hallucination, bias, toxicity"),
    ("RAGAS", "RAG eval: faithfulness, context recall, answer relevancy"),
    ("Promptfoo", "Eval runner across models"),
    ("LangSmith", "Trace every LLM call"),
]))
story.append(subhead("Agentic"))
story.append(tools_table([
    ("LangGraph ★", "Graph-based agent orchestration with state"),
    ("AutoGen (Microsoft)", "Multi-agent — supervisor + specialist"),
    ("CrewAI", "Role-based multi-agent — fast prototyping"),
]))
story.append(subhead("Responsible AI ★"))
story.append(tools_table([
    ("Fairlearn ★", "Fairness toolkit — demographic parity, equalized odds"),
    ("AIF360 (IBM) ★", "70+ fairness metrics, 10+ bias mitigation algorithms"),
    ("What-If Tool (Google) ★", "Visual fairness exploration"),
]))
story.append(subhead("Safety ◆"))
story.append(tools_table([
    ("PyRIT (Microsoft) ◆", "Red-teaming toolkit for GenAI applications"),
    ("Rebuff ◆", "Prompt injection detection — protect RAG and agents"),
    ("LLM Guard ◆", "Input/output scanner — 20+ risk categories"),
    ("Guardrails AI", "Open-source output validation and guardrails"),
    ("presidio", "PII detection and anonymization"),
]))
story.append(PageBreak())
story.append(h2("Projects"))
story.append(bullets([
    "Eval Pipeline: RAGAS test suite for Month 11 RAG — measure and fix lowest scores",
    "LangGraph Agent: Research agent — web search, reads 3 pages, cites sources",
    "★ Fairness Audit: Run Fairlearn on Month 5 Medical Diagnosis model",
    "◆ Red-Team: Use Giskard/PyRIT to find vulnerabilities in RAG chatbot",
    "◆ Safety Layer: Guardrails AI + Rebuff prompt injection detection for agent pipeline",
]))
story.append(h2("Resources"))
story.append(bullets([
    "DeepEval docs | RAGAS docs | LangGraph docs",
    "Fairlearn docs (fairlearn.org) | AIF360 docs (IBM)",
    "◆ PyRIT docs (github.com/Azure/PyRIT) | OWASP Top 10 for LLMs",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "Built automated eval suite using RAGAS",
    "Built LangGraph agent completing multi-step research task",
    "★ Ran fairness audit on real model — documented and mitigated bias",
    "◆ Red-teamed LLM application — structured vulnerability report",
    "◆ Know all OWASP Top 10 for LLMs — can discuss in interview",
]))
story.append(PageBreak())

# ---------------- PHASE 5 ----------------
story.append(phase_banner("◆ Phase 5", "MLOps & Production Deployment ◆ GenAI Enhanced", "Months 14–16"))
story.append(Spacer(1, 10))
story.append(why_box(
    "Deploy models to production, containerize, use cloud, implement CI/CD, monitor. This makes you an ML "
    "engineer not just a data scientist. GenAI additions: streaming SSE, LLM gateway, GenAI monitoring."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "Docker, FastAPI, cloud (AWS/GCP), CI/CD with GitHub Actions",
    "MLflow experiment tracking, DVC data versioning, model registry",
    "Monitoring: data drift (Evidently), Grafana dashboards, Prometheus alerts",
    "★ Open Source contribution — merged PR in LangChain, HuggingFace, or scikit-learn",
    "◆ Streaming LLM endpoints — Server-Sent Events (SSE) for token-by-token output",
    "◆ LLM gateway — LiteLLM proxy: route providers, rate limit, cost tracking",
    "◆ GenAI monitoring — token usage, cost per request, hallucination rate, latency p95",
]))
story.append(h2("Tools & Libraries"))
story.append(subhead("API & Serving"))
story.append(tools_table([
    ("FastAPI", "REST APIs — prediction endpoints, health checks, auto-docs"),
    ("uvicorn", "ASGI server for FastAPI"),
    ("pydantic", "Request/response validation"),
    ("◆ LangServe", "Deploy LangChain chains as FastAPI endpoints"),
    ("◆ BentoML", "ML/LLM service serving with automatic batching"),
]))
story.append(subhead("Infrastructure"))
story.append(tools_table([
    ("Docker", "Package model + code + dependencies"),
    ("Docker Compose", "Multi-container apps locally"),
    ("GitHub Actions", "CI/CD — auto-test and deploy on push"),
    ("◆ Modal", "Serverless GPU/CPU — pay per second, scale to zero"),
    ("◆ Runpod", "Affordable GPU cloud for training and inference"),
]))
story.append(PageBreak())
story.append(subhead("Monitoring"))
story.append(tools_table([
    ("MLflow", "Experiment tracking, model registry"),
    ("DVC", "Dataset + model versioning"),
    ("Evidently AI", "Data drift + model performance monitoring"),
    ("Grafana", "Monitoring dashboards"),
    ("Prometheus", "Metrics collection"),
    ("◆ LiteLLM Proxy", "Unified LLM API gateway — cost tracking, rate limiting"),
    ("◆ Helicone", "LLM observability — cost dashboards, latency tracking"),
]))
story.append(h2("Projects"))
story.append(bullets([
    "Month 14: FastAPI serving + Docker + MLflow experiment tracking",
    "Month 15: Cloud deployment (AWS/GCP) + batch pipeline + monitoring dashboard",
    "Month 16: End-to-end MLOps capstone (churn/fraud/recommendation)",
    "◆ Deploy RAG as streaming FastAPI SSE endpoint (token-by-token output)",
    "◆ LiteLLM Proxy gateway + LangSmith tracing + cost dashboard",
]))
story.append(h2("Resources"))
story.append(bullets([
    "MLOps Zoomcamp (FREE — github.com/DataTalksClub/mlops-zoomcamp)",
    "DeepLearning.AI 'ML Engineering for Production' (audit free)",
    "'Designing ML Systems' by Chip Huyen | ◆ LiteLLM docs | ◆ Modal docs",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "Deployed ≥2 models to cloud with live endpoints",
    "Built end-to-end ML pipeline (data → train → deploy → monitor)",
    "★ Merged open source contribution — linked in GitHub profile",
    "◆ Deployed GenAI app with streaming SSE + LLM gateway + cost tracking",
]))
story.append(PageBreak())

# ---------------- PHASE 5.5 ----------------
story.append(phase_banner("★◆ Phase 5.5", "Inference Optimization & GenAI Cost Management", "Months 16–17 | NEW + Enhanced"))
story.append(Spacer(1, 10))
story.append(why_box(
    "'How would you cut inference costs by 10x?' is now a standard interview question. GenAI cost "
    "management is equally critical — LLM API bills can exceed infrastructure costs at scale."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "Quantization: INT8, INT4, GPTQ, AWQ — reduce model size with minimal accuracy loss",
    "vLLM: PagedAttention + continuous batching — 10–20x LLM throughput",
    "◆ Prompt caching (Anthropic/OpenAI) — 90% cost reduction on repeated system prompts",
    "◆ Batch API (OpenAI/Anthropic) — 50% cost reduction for async/offline workloads",
    "◆ Model routing — cheap small models for simple queries, expensive for complex",
    "◆ Speculative decoding — small draft + large verify model for 2–3x throughput",
]))
story.append(h2("Tools & Libraries"))
story.append(subhead("Quantization"))
story.append(tools_table([
    ("bitsandbytes", "INT4/INT8 — one line of code"),
    ("auto-gptq", "GPTQ post-training quantization"),
    ("autoawq", "AWQ — better accuracy than GPTQ"),
    ("llama.cpp", "Quantized GGUF on CPU"),
    ("Ollama", "User-friendly llama.cpp wrapper"),
]))
story.append(subhead("Inference Servers"))
story.append(tools_table([
    ("vLLM ★", "PagedAttention + continuous batching — 10–20x throughput"),
    ("TensorRT (NVIDIA)", "Up to 6x GPU speedup"),
    ("ONNX Runtime", "Hardware-agnostic model format"),
    ("◆ SGLang", "RadixAttention — better KV cache than vLLM for complex prompts"),
    ("◆ TensorRT-LLM", "NVIDIA — up to 8x faster on A100/H100"),
]))
story.append(subhead("Caching & Cost ◆"))
story.append(tools_table([
    ("Redis", "Semantic response caching"),
    ("GPTCache", "Cache by embedding similarity"),
    ("LiteLLM", "Model routing proxy"),
    ("◆ Anthropic Prompt Caching", "90% cost + 85% latency reduction on repeated context"),
    ("◆ OpenAI Prompt Caching", "50% cost reduction for prompts >1024 tokens"),
    ("◆ Batch API", "50% cost reduction for async workloads"),
    ("tiktoken", "Count tokens before API calls — control cost"),
]))
story.append(PageBreak())
story.append(h2("Projects"))
story.append(bullets([
    "Optimize Month 11 RAG: (1) Quantized GGUF model via llama.cpp",
    "(2) Semantic caching with Redis — measure cache hit rate",
    "(3) Model routing: simple → GPT-4o-mini/Haiku, complex → GPT-4o/Sonnet",
    "(4) Enable Anthropic/OpenAI prompt caching — document cost reduction",
    "(5) Move batch eval jobs to Batch API — document 50% cost saving",
    "(6) Measure latency p50/p95, throughput (req/s), cost/query before vs after each step",
]))
story.append(h2("Resources"))
story.append(bullets([
    "vLLM docs (docs.vllm.ai) | llama.cpp GitHub | DeepLearning.AI Quantization course (free)",
    "◆ Anthropic Prompt Caching docs | ◆ OpenAI Batch API docs | ◆ SGLang docs",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "Can explain quantization trade-offs clearly in an interview",
    "Deployed vLLM and benchmarked throughput improvement",
    "◆ Implemented semantic caching — measured cache hit rate and cost reduction",
    "◆ Used Batch API — documented 50% cost savings",
    "◆ Built model router selecting models by query complexity",
]))
story.append(PageBreak())

# ---------------- PHASE 5.8 ----------------
story.append(phase_banner("★◆ Phase 5.8", "ML System Design — 9-Step Framework + 8 Worked Examples", "Month 17 | NEW + GenAI Designs"))
story.append(Spacer(1, 10))
story.append(why_box(
    "ML System Design is the most-tested skill at final-round ML interviews and entirely absent from most "
    "self-taught roadmaps. 5 classic ML designs + 3 GenAI-specific designs."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "Master the 9-step ML system design framework",
    "Practice 5 ML designs: recommendation, fraud, semantic search, RAG chatbot, content moderation",
    "◆ Practice 3 GenAI designs: LLM Copilot (Cursor-style), GenAI content pipeline, Voice AI agent",
    "Draw architecture diagrams confidently on whiteboard or shared screen",
    "Know trade-offs: batch vs real-time, two-tower vs cross-encoder, BM25 vs dense retrieval",
    "Add fairness (Fairlearn) and EU AI Act compliance to every design",
]))
story.append(h2("Tools & Libraries"))
story.append(subhead("Diagramming"))
story.append(tools_table([
    ("Excalidraw", "Free whiteboard — draw system designs in interviews"),
    ("draw.io / diagrams.net", "Free diagrams — export to PNG for GitHub READMEs"),
    ("Whimsical", "Clean flowcharts for design docs"),
    ("Mermaid.js", "Diagrams as code — auto-renders in GitHub Markdown"),
]))
story.append(subhead("Reference"))
story.append(tools_table([
    ("ML System Design Interview book", "Ali Aminian — most targeted book"),
    ("Designing ML Systems (Chip Huyen)", "Best production ML thinking book"),
    ("ByteByteGo", "System design fundamentals complement ML knowledge"),
    ("Qdrant / Weaviate / Pinecone", "Know one vector DB in depth for RAG/search designs"),
    ("Feast (Feature Store)", "Understand offline vs online feature store split"),
]))
story.append(h2("Projects"))
story.append(bullets([
    "Draw all 8 system designs as Excalidraw architecture diagrams",
    "Record yourself explaining one design end-to-end in 45 minutes",
    "Write ML system design blog post on Hashnode",
    "◆ Extend GenAI designs with cost optimization and prompt caching sections",
]))
story.append(h2("Resources"))
story.append(bullets([
    "'ML System Design Interview' by Ali Aminian & Alex Xu — TOP PRIORITY",
    "'Designing ML Systems' by Chip Huyen | Evidently AI blog | Eugene Yan blog",
    "◆ Simon Willison's blog | ◆ Hamel Husain's blog — LLM production patterns",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "Can walk through complete ML system design in 45 minutes",
    "Drew architecture diagrams for all 5 ML + 3 GenAI worked examples",
    "Can explain trade-offs: batch vs real-time, BM25 vs dense, two-tower vs cross-encoder",
    "◆ Can design LLM Copilot, GenAI content pipeline, Voice AI Agent (<500ms latency budget)",
]))
story.append(PageBreak())

# ---------------- PHASE 6 ----------------
story.append(phase_banner("★◆ Phase 6", "Job Prep, Portfolio & Career Launch", "Month 17+ | NEW + GenAI Portfolio"))
story.append(Spacer(1, 10))
story.append(why_box(
    "Package everything into a story that lands the job. Portfolio website, technical writing, and GenAI "
    "demos — every skill from Phases 0–5.8 now becomes your competitive advantage."))
story.append(h2("Learning Objectives"))
story.append(bullets([
    "Polish top 6 GitHub projects incl. Nepali NLP + NLP API + CV pipeline",
    "★ Build portfolio website (username.github.io) with project cards and live demo links",
    "LeetCode: 30–40 easy + 20–30 medium — arrays, trees, hashmaps, sliding window",
    "★ Data privacy & GDPR-style principles — lawful bases, right to erasure, PII, differential privacy",
    "EU AI Act risk tiers — high-risk documentation requirements, fairness obligations",
    "★ Technical writing — 1 Hashnode/Medium post per project = 6 async interviews",
    "◆ GenAI portfolio: RAG+Eval + multimodal pipeline + voice demo + prompt engineering",
    "◆ Blog priority: 'How I reduced LLM API costs by 60%' — highest traffic GenAI topic 2026",
]))
story.append(h2("Tools & Libraries"))
story.append(subhead("Portfolio ★"))
story.append(tools_table([
    ("GitHub Pages", "Free hosting — push to gh-pages branch"),
    ("Jekyll / al-folio", "Best academic portfolio template — free"),
    ("Shields.io", "GitHub README badges — Python version, license"),
    ("README.so", "Interactive README builder"),
]))
story.append(subhead("Technical Writing ★"))
story.append(tools_table([
    ("Hashnode ◆", "Developer blogging — SEO-friendly, custom domain, free"),
    ("Medium / TDS", "Large ML audience — submit to Towards Data Science"),
    ("Grammarly", "Grammar + clarity checker — use before every post"),
    ("Hemingway App", "Readability — aim Grade 8 level for reach"),
]))
story.append(PageBreak())
story.append(subhead("Job Search"))
story.append(tools_table([
    ("LinkedIn", "Primary — set target locations, enable Open to Work"),
    ("Wellfound", "Startup and tech jobs across markets"),
    ("Company career pages", "Apply directly to target companies' listings"),
]))
story.append(subhead("Data Privacy (GDPR-style principles) ★"))
story.append(tools_table([
    ("gdpr-info.eu", "Full GDPR text annotated — free"),
    ("ICO AI guidance", "AI and data protection guide — free PDF"),
    ("presidio", "PII detection library"),
    ("artificialintelligenceact.eu", "EU AI Act full text — know risk tiers"),
]))
story.append(h2("Projects"))
story.append(bullets([
    "Build portfolio website with GitHub Pages (al-folio theme recommended)",
    "Write 6 blog posts — one per major project — before applications start",
    "Prepare 3-minute live demo of best GenAI project (voice or multimodal)",
    "Target 5–10 quality applications per week from Month 18",
    "Mock interviews: Pramp — 5+ sessions (coding, ML, system design)",
]))
story.append(h2("Resources"))
story.append(bullets([
    "NeetCode (neetcode.io) | 'ML System Design Interview' by Ali Aminian",
    "LinkedIn + Wellfound + company career pages",
    "gdpr-info.eu | artificialintelligenceact.eu",
    "al-folio Jekyll theme (GitHub) | Towards Data Science submission guide",
]))
story.append(h2("Success Metrics"))
story.append(metrics_block([
    "★ Portfolio website live at username.github.io with 6 projects",
    "★ 6 technical blog posts published on Hashnode/Medium",
    "Can design any of the 8 ML + GenAI systems in 45 minutes",
    "Applied to 50+ positions | Completed 5+ technical interviews",
    "◆ ≥2 GenAI projects with live demos ready for interview",
    "Received a strong job offer with a salary matching market rate for the role",
]))
story.append(PageBreak())

# ---------------- SUMMARY ----------------
story.append(h2("Complete Additions Summary — All 33 Original + 2 New Deep Dive Phases"))
summary_rows = [
    ("#", "Addition", "Phase", "Type"),
    ("1–13", "All original ★ additions (SQL, Tabular, Annotation, GNNs, Structured Outputs, Fairness, "
             "Inference Opt., System Design, Portfolio, Blog, EU AI Act, GNN project, Nepali Label Studio)",
     "Various", "★ Original"),
    ("14–19", "GenAI: Diffusion, Multimodal LLMs, Audio AI, Phase 4.2 Prompt Eng., DSPy, "
              "PromptFlow/Promptfoo/LangSmith", "Phase 4 + 4.2", "◆ GenAI"),
    ("20–25", "GenAI Safety: PyRIT, Rebuff, LLM Guard, HELM, lm-eval, Giskard", "Phase 4.5", "◆ GenAI"),
    ("26–28", "MLOps GenAI: LangServe, BentoML, Modal, SSE streaming, LiteLLM, Helicone", "Phase 5", "◆ GenAI"),
    ("29–31", "Inference GenAI: SGLang, TensorRT-LLM, Runpod, Batch API, Prompt Caching", "Phase 5.5", "◆ GenAI"),
    ("32–33", "System Design GenAI: LLM Copilot, Content Pipeline, Voice Agent designs", "Phase 5.8", "◆ GenAI"),
    ("35", "▲ NLP Deep Dive — Classical NLP, Word2Vec/GloVe/FastText, mBERT, XLM-R, IndicBERT, IndicNLP, "
           "Stanza Nepali, 7 tool categories, Nepali NER project, FastText Nepali embeddings, NLP API deployment",
     "Phase 3.5 (NEW)", "▲ NLP New"),
    ("36", "■ CV Deep Dive — OpenCV classical CV, YOLOv8/v11 detection, SAM segmentation, MediaPipe pose, "
           "PaddleOCR/TrOCR, Depth Anything, video tracking, ONNX/TensorRT production, Nepali OCR pipeline",
     "Phase 3.6 (NEW)", "■ CV New"),
]
data = [[Paragraph(f"<b>{c}</b>", styles["TableHeadCell"]) for c in summary_rows[0]]]
for row in summary_rows[1:]:
    data.append([Paragraph(row[0], styles["TableCellBold"]), Paragraph(row[1], styles["TableCell"]),
                 Paragraph(row[2], styles["TableCell"]), Paragraph(row[3], styles["TableCell"])])
t = Table(data, colWidths=[0.5*inch, 4.4*inch, 1.2*inch, 1.4*inch], repeatRows=1)
tstyle = [
    ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEAD_COLOR),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]
for i in range(1, len(data)):
    if i % 2 == 0:
        tstyle.append(("BACKGROUND", (0, i), (-1, i), TABLE_ALT_COLOR))
t.setStyle(TableStyle(tstyle))
story.append(t)
story.append(PageBreak())

# ---------------- FINAL THOUGHTS ----------------
story.append(h2("Final Thoughts — You Now Have Everything"))
story.append(body(
    "This is the most complete ML/AI roadmap available. The NLP Deep Dive (Phase 3.5) gives you the "
    "foundation to make your Nepali NLP project world-class. The CV Deep Dive (Phase 3.6) adds Nepali OCR — "
    "a genuinely unique and unsolved problem — to your portfolio. Combined with the GenAI enhancements and "
    "system design training, you now have an end-to-end plan that covers every skill top ML companies test "
    "for. Code every day. Build in public. Evaluate your work."))
story.append(bullets([
    "Code daily — 45 minutes every day beats weekend marathons — non-negotiable",
    "Nepali NLP + OCR — your unique differentiators in any interview",
    "Build in public — HuggingFace Hub + GitHub + Hashnode — 6 blog posts = 6 async interviews",
    "GenAI depth — diffusion + voice + multimodal demos are memorable and rare",
    "Evaluate everything — RAGAS, DeepEval, Promptfoo — evals separate juniors from seniors",
    "System design fluency — final rounds won or lost here — practice all 8 designs weekly",
    "NLP foundations — classical NLP + word embeddings make your LLM work 10x deeper",
    "CV production skills — ONNX + TensorRT + YOLOv8 = credible in industry CV interviews",
    "Audit for fairness — Responsible AI is increasingly a baseline expectation",
    "Be patient — 18–22 months is realistic — trust the process, compare to past you",
]))
story.append(Spacer(1, 10))
story.append(body(
    "First job goal: Junior ML/AI Engineer or LLM Application Developer, with a competitive salary "
    "matching market rate. Your Nepali NLP expertise and GenAI depth make you memorable. Every day of "
    "coding brings you closer."))

# ---------------- BUILD ----------------
PAGE_W, PAGE_H = letter

def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawString(0.75*inch, 0.5*inch, "ML/AI Roadmap — Ultimate + NLP & CV Deep Dive 2026")
    canvas.drawCentredString(PAGE_W/2, 0.5*inch, "Prepared by Rabi Sah")
    canvas.drawRightString(PAGE_W - 0.75*inch, 0.5*inch, f"Page {doc.page}")
    canvas.setStrokeColor(colors.HexColor("#cccccc"))
    canvas.line(0.75*inch, 0.62*inch, PAGE_W - 0.75*inch, 0.62*inch)
    canvas.restoreState()

doc = SimpleDocTemplate("/mnt/user-data/outputs/ML_AI_Roadmap_NLP_CV_2026.pdf",
                         pagesize=letter,
                         leftMargin=0.75*inch, rightMargin=0.75*inch,
                         topMargin=0.7*inch, bottomMargin=0.85*inch,
                         title="ML/AI Roadmap — Ultimate + NLP & CV Deep Dive 2026",
                         author="Rabi Sah")

doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)
print("PDF built successfully")