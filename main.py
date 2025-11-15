import csv
import json
import datetime
import sys
from pathlib import Path
from io import StringIO

LOG_FILENAME = "mission_computer_main.log"
OUT_JSON = "mission_computer_main.json"

def parse_timestamp(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    except Exception:
        return None

def main():
    base = Path(__file__).parent
    log_path = base / LOG_FILENAME

    try:
        # 시도: UTF-8로 읽기
        text = log_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: '{LOG_FILENAME}' 파일을 찾을 수 없습니다.", file=sys.stderr)
        return
    except UnicodeDecodeError:
        # 디코딩 오류 발생시 안전하게 읽기(대체 문자)
        try:
            text = log_path.read_text(encoding="utf-8", errors="replace")
            print("Warning: 디코딩 오류 발생. 손상된 문자는 대체 문자로 읽었습니다.", file=sys.stderr)
        except Exception as e:
            print(f"Error reading file with fallback: {e}", file=sys.stderr)
            return
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        return

    # 전체 내용 출력
    print("=== Raw log file content ===")
    print(text)

    # CSV 파싱
    reader = csv.reader(StringIO(text))
    items = []
    for i, row in enumerate(reader):
        if not row:
            continue
        # 헤더 스킵(첫 줄이 'timestamp'로 시작하면)
        if i == 0 and row[0].strip().lower() == "timestamp":
            continue
        # timestamp는 첫 열, message는 마지막 열로 취급
        ts = row[0].strip()
        msg = row[-1].strip() if len(row) >= 2 else ""
        items.append([ts, msg])

    # 리스트 객체 출력
    print("\n=== Parsed list (timestamp, message) ===")
    print(items)

    # 시간 역순 정렬
    def sort_key(pair):
        dt = parse_timestamp(pair[0])
        # 파싱 실패 시 최소값 사용하여 맨 뒤로 보내기
        return dt if dt is not None else datetime.datetime.min

    sorted_items = sorted(items, key=sort_key, reverse=True)
    print("\n=== Sorted list (reverse chronological) ===")
    print(sorted_items)

    # 사전으로 변환 (정렬된 순서 유지)
    ordered_dict = {ts: msg for ts, msg in sorted_items}
    print("\n=== Dict object (to be saved) ===")
    print(ordered_dict)

    # JSON으로 저장 (UTF-8)
    try:
        out_path = base / OUT_JSON
        out_path.write_text(json.dumps(ordered_dict, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nSaved JSON to: {out_path}")
    except Exception as e:
        print(f"Error writing JSON file: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()