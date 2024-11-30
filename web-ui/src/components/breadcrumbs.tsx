"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

function DividerSVG() {
  return (
    <svg
      viewBox="0 0 24 44"
      preserveAspectRatio="none"
      aria-hidden="true"
      className="h-full w-6 shrink-0 text-lime-800"
    >
      <path
        d="M.293 0l22 22-22 22h1.414l22-22-22-22H.293z"
        stroke="currentColor"
        strokeWidth="2"
      />
    </svg>
  );
}

const Breadcrumbs = () => {
  const pathname = usePathname();
  const breadcrumbSegments = pathname.split("/").filter(Boolean);

  return (
    <nav aria-label="Breadcrumb" className="flex h-11 bg-gray-900">
      <ol
        role="list"
        className="mx-auto flex w-full max-w-screen-xl space-x-4 px-4 sm:px-6 lg:px-8"
      >
        <li className="flex">
          <div className="flex items-center">
            <Link
              href="/"
              className="text-gray-400 hover:text-gray-300 font-medium text-lg"
            >
              HOME
            </Link>
          </div>
        </li>
        {breadcrumbSegments.map((segment, index) => {
          const path = `/${breadcrumbSegments.slice(0, index + 1).join("/")}`;
          const isCurrentPage = index === breadcrumbSegments.length - 1;
          const breadcrumbName = decodeURIComponent(segment)
            .toUpperCase()
            .replace("-", " ");

          return (
            <li key={path} className="flex">
              <div className="flex items-center">
                <DividerSVG />
                <Link
                  href={path}
                  aria-current={isCurrentPage ? "page" : undefined}
                  className="ml-4 text-lg font-medium text-gray-400 hover:text-gray-300"
                >
                  {breadcrumbName}
                </Link>
              </div>
            </li>
          );
        })}
      </ol>
    </nav>
  );
};

export default Breadcrumbs;
