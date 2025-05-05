from pathlib import Path

# Load the Rmd file
file_path = Path("cleaned_path.rmd")
rmd_content = file_path.read_text()

# Fix the LaTeX math issue
# Replace problematic math fragments with correctly formatted inline math
import re

# This pattern looks for LaTeX text that ends with \texttt{...} followed by a \)
pattern = r"(\\texttt\{posterior_mean_theta\})\s*\\\)"

# Add the missing $ signs around the whole expression if not already present
corrected_content = re.sub(r"eta\s+\\approx\s+" + pattern, r"$\\theta \\approx \1$", rmd_content)

# Save the corrected version
corrected_file_path = Path("/mnt/data/HM1sds-2_cleaned_fixed.Rmd")
corrected_file_path.write_text(corrected_content)

corrected_file_path.name
