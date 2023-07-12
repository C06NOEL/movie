import sqlite3
import random

class Recommand_System():
    def __init__(self):
        self.conn = sqlite3.connect('Movies.db')
        self.cursor = self.conn.cursor()

    def cleanmsg(self, msg):
        msg=msg
        row_msg = msg.strip().split('\n')
        result = {item.split('：')[0]: item.split('：')[1].strip() for item in row_msg}
        return result

    # 推薦
    def random_recommand(self, dict:dict = {}):
        # 匯入使用者限搜

        year = dict.get('年度')
        chinese_title = dict.get('中文片名')
        original_title = dict.get('原文片名')
        country = dict.get('國別')
        language = dict.get('語言')
        genre = dict.get('類型')

        query = "SELECT 年度,中文片名,原文片名,國別,語言,類型 FROM Movies_latest WHERE 1=1"
        params = []

        # 年度搜索
        if year:
            if '-' in year:
                # 年份範圍搜索
                start_year, end_year = year.split('-')
                query += " AND 年度 BETWEEN ? AND ?"
                params.extend([start_year, end_year])
            elif year.endswith('>'):
                # 某年之後搜索
                year_offset = year[:-1]
                query += " AND 年度 >= ?"
                params.append(year_offset)
            elif year.endswith('<'):
                # 某年之前搜索
                year_offset = year[:-1]
                query += " AND 年度 <= ?"
                params.append(year_offset)
            else:
                # 指定某年
                query += " AND 年度 = ?"
                params.append(year)

        # 可模糊搜尋
        if chinese_title:
            query += " AND 中文片名 LIKE '%' || ? || '%'"
            params.append(chinese_title)

        # 可模糊搜尋
        if original_title:
            query += " AND 原文片名 LIKE '%' || ? || '%'"
            params.append(original_title)

        # 可模糊搜尋
        if country:
            query += " AND 國別 LIKE '%' || ? || '%'"
            params.append(country)

        # 可模糊搜尋
        if language:
            query += " AND 語言 LIKE '%' || ? || '%'"
            params.append(language)

        # 可多重搜尋
        if genre:
            genre_keywords = genre.split()
            for keyword in genre_keywords:
                query += " AND 類型 LIKE '%' || ? || '%'"
                params.append(keyword)


        self.cursor.execute(query, params)
        results = self.cursor.fetchall()
        self.conn.close()

        if not results: return "無結果"

        # 隨機從限搜下推3個
        # 有重複名稱就從新隨機(英文片名判斷)
        if len(results) > 3:
            while True:
                random_results = random.sample(results, 3)
                check = set([item[2] for item in random_results])
                if len(check) == 3: break
        else:
            random_results = results

        result = '\n'.join([' | '.join(map(str, tpl)) for tpl in random_results])
        return result