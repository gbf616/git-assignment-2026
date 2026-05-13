import csv

class StudentGradeManager:
    """
    学生成績管理システム（Git演習用）
    機能：
      - 生徒の追加（入力検証付き）
      - 個人平均点・クラス平均点の計算
      - 生徒一覧取得
      - CSVファイルへのエクスポート
    """

    def __init__(self):
        """初期化：空の生徒データを準備"""
        self.students = {}

    def add_student(self, name: str, grades: list):
        """
        生徒を追加する（厳格な入力検証付き）
        
        Parameters:
            name (str): 生徒名（空文字不可）
            grades (list): 成績のリスト（0〜100の数値のみ）
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("生徒名は空文字にできません")
        
        if (not isinstance(grades, list) or 
            not all(isinstance(g, (int, float)) and 0 <= g <= 100 for g in grades)):
            raise ValueError("成績は0〜100の数値のリストである必要があります")
        
        self.students[name.strip()] = grades
        print(f"✅ {name.strip()} を追加しました")

    def calculate_average(self, name: str):
        """指定生徒の平均点を計算"""
        if name not in self.students or not self.students[name]:
            return None
        return sum(self.students[name]) / len(self.students[name])

    def get_class_average(self):
        """クラス全体の平均点を計算"""
        if not self.students:
            return None
        total = sum(sum(grades) for grades in self.students.values())
        count = sum(len(grades) for grades in self.students.values())
        return total / count if count > 0 else None

    def list_all_students(self):
        """全生徒の名前一覧を返す"""
        return list(self.students.keys())

    def export_to_csv(self, filename="grades.csv"):
        """
        成績データをCSVファイルにエクスポート
        """
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['生徒名', '成績リスト', '平均点'])
            for name, grades in self.students.items():
                avg = self.calculate_average(name)
                writer.writerow([name, grades, f"{avg:.2f}" if avg is not None else ""])
        print(f"📁 CSVエクスポート完了 → {filename}")

    def show_all(self):
        """現在の全生徒データを表示（デバッグ用）"""
        print("\n=== 現在の生徒データ ===")
        for name, grades in self.students.items():
            avg = self.calculate_average(name)
            print(f"  {name}: {grades} → 平均 {avg:.2f}点" if avg else f"  {name}: {grades}")


# ==================== テスト実行（課題提出時に便利） ====================
if __name__ == "__main__":
    manager = StudentGradeManager()
    
    # テストデータ追加
    manager.add_student("田中太郎", [85, 92, 78, 88])
    manager.add_student("佐藤花子", [90, 95, 87])
    manager.add_student("鈴木次郎", [70, 82, 91, 65])
    
    # 各種機能テスト
    print(f"クラス平均: {manager.get_class_average():.2f}点")
    print("全生徒一覧:", manager.list_all_students())
    
    manager.show_all()
    manager.export_to_csv()
    
    print("\n🎉 StudentGradeManager の全機能テスト完了！")