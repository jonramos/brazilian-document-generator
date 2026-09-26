import random

CNPJ_BLACKLIST = {"add-cnpj-here"}

def generate_cpf() -> str:
	while True:
		digits = [random.randint(0, 9) for _ in range(9)]
		if len(set(digits)) > 1:
			break

	for weight in (10, 11):
		checksum = sum(digit * factor for digit, factor in zip(digits, range(weight, 1, -1)))
		check_digit = (checksum * 10) % 11
		digits.append(0 if check_digit == 10 else check_digit)

	cpf = "".join(map(str, digits))
	return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def generate_cnpj() -> str:
	while True:
		digits = [random.randint(0, 9) for _ in range(12)]
		if len(set(digits)) == 1:
			continue

		for weights in ((5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2), (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)):
			checksum = sum(digit * weight for digit, weight in zip(digits, weights))
			remainder = checksum % 11
			digits.append(0 if remainder < 2 else 11 - remainder)

		cnpj = "".join(map(str, digits))
		formatted_cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
		if formatted_cnpj not in CNPJ_BLACKLIST:
			return formatted_cnpj


def generate_alphanumeric_cnpj() -> str:
	characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	while True:
		base = [random.choice(characters) for _ in range(12)]
		if len(set(base)) == 1:
			continue

		values = [ord(character) - ord("0") for character in base]
		for weights in ((5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2), (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)):
			checksum = sum(value * weight for value, weight in zip(values, weights))
			remainder = checksum % 11
			check_digit = 0 if remainder < 2 else 11 - remainder
			base.append(str(check_digit))
			values.append(check_digit)

		cnpj = "".join(base)
		formatted_cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
		if formatted_cnpj not in CNPJ_BLACKLIST:
			return formatted_cnpj