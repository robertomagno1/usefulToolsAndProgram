import re

# Load the file and clean it from problematic Unicode characters for LaTeX
input_path = "/mnt/data/.Rmd"
output_path = "/mnt/data/.Rmd"

# Unicode character replacements
replacements = {
    "≈": r"$\approx$",
    "≠": r"$\neq$",
    "≤": r"$\leq$",
    "≥": r"$\geq$",
    "→": r"$\rightarrow$",
    "←": r"$\leftarrow$",
    "∞": r"$\infty$",
    "∑": r"$\sum$",
    "∈": r"$\in$",
    "∆": r"$\Delta$",
    "°": r"$^\circ$",
    "²": r"$^2$",
    "³": r"$^3$",
    "θ": r"$\theta$",
    "π": r"$\pi$",
    "ψ": r"$\psi$",
    "μ": r"$\mu$",
    "Σ": r"$\Sigma$",
    "α": r"$\alpha$",
    "β": r"$\beta$",
    "→": r"$\to$"
}

# Read the file content
with open(input_path, "r", encoding="utf-8") as file:
    content = file.read()

# Replace Unicode characters with LaTeX-safe equivalents
for char, latex in replacements.items():
    content = content.replace(char, latex)

# Write the cleaned content to a new file
with open(output_path, "w", encoding="utf-8") as file:
    file.write(content)

output_path
