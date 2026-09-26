import tkinter as tk
from generators import *


def main() -> None:
	window = tk.Tk()
	window.title("Gerador de documentos")

	cpf_text = tk.StringVar(value="O número gerado aparecerá aqui")
	controls = tk.Frame(window)
	controls.pack(padx=12, pady=12)

	cpf_button = tk.Button(controls, text="Gerar CPF", command=lambda: cpf_text.set(generate_cpf()))
	cpf_button.pack(side="left", padx=(0, 8))

	cnpj_button = tk.Button(controls, text="Gerar CNPJ", command=lambda: cpf_text.set(generate_cnpj()))
	cnpj_button.pack(side="left", padx=(0, 8))

	alphanumeric_cnpj_button = tk.Button(
		controls,
		text="Gerar CNPJ Alfanumérico",
		command=lambda: cpf_text.set(generate_alphanumeric_cnpj()),
	)
	alphanumeric_cnpj_button.pack(side="left", padx=(0, 8))

	label = tk.Entry(
		controls,
		textvariable=cpf_text,
		state="readonly",
		justify="center",
		relief="flat",
		readonlybackground=window.cget("bg"),
		width=45,
	)
	label.pack(side="right")

	window.mainloop()


if __name__ == "__main__":
	main()
