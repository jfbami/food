import sqlite3
import os

class PhotoAssistantDB:
    def __init__(self, db_path='photoassistant.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS Photos (
            photo_id INTEGER PRIMARY KEY,
            filepath TEXT NOT NULL,
            original_filename TEXT,
            upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            llm_description TEXT,
            source_url TEXT,
            user_rating INTEGER
        )''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS AestheticLabels (
            label_id INTEGER PRIMARY KEY,
            label_name TEXT NOT NULL,
            label_description TEXT
        )''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS CompositionRules (
            rule_id INTEGER PRIMARY KEY,
            rule_name TEXT NOT NULL,
            rule_description TEXT
        )''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS Photo_Labels_Link (
            link_id INTEGER PRIMARY KEY,
            photo_id INTEGER,
            label_id INTEGER,
            label_type TEXT,
            source TEXT,
            confidence REAL,
            FOREIGN KEY (photo_id) REFERENCES Photos (photo_id),
            FOREIGN KEY (label_id) REFERENCES AestheticLabels (label_id)
        )''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS AnalysisResults (
            result_id INTEGER PRIMARY KEY,
            photo_id INTEGER,
            analysis_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            raw_cv_output TEXT,
            generated_feedback TEXT,
            FOREIGN KEY (photo_id) REFERENCES Photos (photo_id)
        )''') 

