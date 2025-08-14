# Steps to Recreate .venv and Install Jupyter Kernel

## Quick Steps to Fix Corrupted Virtual Environment

When your `.venv` becomes corrupted or has package conflicts, follow these platform-specific steps to recreate it.

**Important:** All commands should be run from the `agenticAIeducation` directory (the directory containing this file).

---

## Windows Instructions

### Step-by-Step Commands
From the `agenticAIeducation` directory:

```powershell
# 1. Remove the corrupted environment (if it exists)
powershell -Command "if (Test-Path .venv) { Remove-Item -Recurse -Force .venv }"

# 2. Create a fresh virtual environment
uv venv .venv

# 3. Install Jupyter kernel
uv pip install ipykernel

# 4. Register as Jupyter kernel (note the backslashes and .exe extension)
powershell -Command ".venv\Scripts\python.exe -m ipykernel install --user --name agentic_ai_education --display-name 'Agentic AI Education'"
```

### All Windows Commands in One Block
```powershell
# Run from agenticAIeducation directory
powershell -Command "if (Test-Path .venv) { Remove-Item -Recurse -Force .venv }"
uv venv .venv
uv pip install ipykernel
powershell -Command ".venv\Scripts\python.exe -m ipykernel install --user --name agentic_ai_education --display-name 'Agentic AI Education'"
```

---

## Mac/Linux Instructions

### Step-by-Step Commands
From the `agenticAIeducation` directory:

```bash
# 1. Remove the corrupted environment (if it exists)
rm -rf .venv

# 2. Create a fresh virtual environment
uv venv .venv

# 3. Install Jupyter kernel
uv pip install ipykernel

# 4. Register as Jupyter kernel (note the forward slashes)
.venv/bin/python -m ipykernel install --user --name agentic_ai_education --display-name "Agentic AI Education"
```

### All Mac/Linux Commands in One Block
```bash
# Run from agenticAIeducation directory
rm -rf .venv
uv venv .venv
uv pip install ipykernel
.venv/bin/python -m ipykernel install --user --name agentic_ai_education --display-name "Agentic AI Education"
```

---

## Path Differences Between Platforms

| Component | Windows Path | Mac/Linux Path |
|-----------|-------------|----------------|
| Python executable | `.venv\Scripts\python.exe` | `.venv/bin/python` |
| Activation script | `.venv\Scripts\activate` | `.venv/bin/activate` |
| pip executable | `.venv\Scripts\pip.exe` | `.venv/bin/pip` |

---

## When to Use This
- When you see "Access is denied" errors during package installation
- When packages have missing or corrupted METADATA files
- When Jupyter shows "requires the ipykernel package" error
- When package dependencies are broken beyond repair
- When switching between Python versions

## After Completion
1. Restart VS Code or Jupyter
2. Select "Agentic AI Education" from the kernel dropdown
3. Install any additional packages needed for your project using `uv pip install <package-name>`

## Troubleshooting
- **Windows:** If PowerShell commands fail, ensure you're running from an elevated prompt or have execution policies set correctly
- **Mac/Linux:** If permission denied, you may need to use `sudo` for the kernel installation step
- **Both:** Ensure `uv` is installed and available in your PATH