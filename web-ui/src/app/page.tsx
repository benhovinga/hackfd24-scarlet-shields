import Link from "next/link";

type DashboardTools = {
  name: string;
  href: string;
  description: string;
  icon: string;
  disabled?: boolean;
}[];

const dashboardTools: DashboardTools = [
  {
    name: "Network scan",
    href: "nmap",
    description: "Uses NMAP to scan a network",
    icon: "todo",
  },
  {
    name: "Identify MAC addresses",
    href: "#",
    description: "Uses Better Cap to identify MAC address of IP",
    icon: "todo",
  },
  {
    name: "Attack",
    href: "#",
    description: "Uses Metasploit to deliver a payload",
    icon: "todo",
  },
  { name: "TBD", href: "#", description: "TBD", icon: "todo", disabled: true },
];

export default function Dashboard() {
  return (
    <>
      <h2 className="text-4xl">Dashboard</h2>
      <ul
        role="list"
        className="mt-3 grid grid-cols-1 gap-5 sm:grid-cols-2 sm:gap-6 lg:grid-cols-4"
      >
        {dashboardTools.map((tool) => (
          <li key={tool.name} className="">
            <Link href={tool.href} className="col-span-1 flex rounded-md">
              <div className="flex w-16 shrink-0 items-center justify-center rounded-l-md text-sm font-medium text-white bg-lime-900">
                {tool.icon}
              </div>
              <div className="flex flex-1 items-center justify-between truncate rounded-r-md border-b border-r border-t border-gray-700 bg-gray-900">
                <div className="flex-1 truncate px-4 py-2 text-xl font-medium text-white hover:text-gray-300">
                  {tool.name}
                  <p className="text-gray-400 text-base">{tool.description}</p>
                </div>
              </div>
            </Link>
          </li>
        ))}
      </ul>
    </>
  );
}
