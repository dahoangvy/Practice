def main():
    input_path = "NOODLE_CONTEST/BAI01.INP"
    output_path = "NOODLE_CONTEST/BAI01.OUT"

    try:
        with open(input_path, "r") as f:
            scores = [float(score.replace(",", ".")) for score in f.read().split()]

        with open(output_path, "w") as w:
            w.write(f"{len(scores)}\n{max(scores)}\n{scores.count(max(scores))}")

    except FileNotFoundError as e:
        print(f"File {input_path} không tồn tại.")
    except ValueError as e:
        print("Không hợp lệ")

if __name__ == "__main__":
    main()
