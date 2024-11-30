import { spawn } from "child_process";
import { NextRequest, NextResponse } from "next/server";
import { PYTHON_SCRIPT_PATH } from "../../../../config";

// Define the type for the Python script's result
type PythonResult = {
  success: boolean;
  output?: string;
  error?: string;
  code?: number;
};

export async function GET(request: NextRequest): Promise<NextResponse> {
  const searchParams = request.nextUrl.searchParams;
  const ipAddress = searchParams.get("ip");
  if (!ipAddress) {
    return NextResponse.json({ success: false, error: "IP address missing" });
  }

  const pythonProgram = PYTHON_SCRIPT_PATH;
  const args: string[] = ["nmap", ipAddress];

  return new Promise((resolve) => {
    const pythonProcess = spawn("python3", [pythonProgram, ...args]);

    let output = "";
    let error = "";

    // Capture stdout
    pythonProcess.stdout.on("data", (data: Buffer) => {
      output += data.toString();
    });

    // Capture stderr
    pythonProcess.stderr.on("data", (data: Buffer) => {
      error += data.toString();
    });

    // Handle process close
    pythonProcess.on("close", (code: number) => {
      const response: PythonResult =
        code === 0
          ? { success: true, output }
          : { success: false, error, code };

      resolve(NextResponse.json(response, { status: code === 0 ? 200 : 500 }));
    });

    // Handle errors when spawning the process
    pythonProcess.on("error", (err: Error) => {
      resolve(
        NextResponse.json(
          { success: false, error: err.message },
          { status: 500 }
        )
      );
    });
  });
}
