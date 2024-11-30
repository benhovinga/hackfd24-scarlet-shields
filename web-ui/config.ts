import { fileURLToPath } from "url";
import { dirname, resolve } from "path";

const filename = fileURLToPath(import.meta.url);
const currentDirectory = dirname(filename);

const pythonToolkitDir = resolve(currentDirectory, "..", "python-toolkit");
const pythonScript = "script.py";

export const PYTHON_SCRIPT_PATH = `${pythonToolkitDir}/${pythonScript}`;
