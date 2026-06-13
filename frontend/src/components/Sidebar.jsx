import { FileStack, LayoutDashboard, MessageSquareText, ScanSearch, Sparkles, UserRoundSearch } from "lucide-react";
import { NavLink } from "react-router-dom";

const items = [
  { to: "/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { to: "/generate", label: "Question Generator", icon: Sparkles },
  { to: "/resume", label: "Resume Questions", icon: UserRoundSearch },
  { to: "/job-description", label: "Job Description Analyzer", icon: ScanSearch },
  { to: "/mock-interview", label: "Mock Interview", icon: MessageSquareText },
  { to: "/history", label: "History", icon: FileStack },
];

export default function Sidebar() {
  return (
    <aside className="hidden w-72 shrink-0 lg:block">
      <div className="sticky top-24 rounded-3xl border border-white/10 bg-white/5 p-4 shadow-panel">
        <p className="px-3 pb-3 text-xs uppercase tracking-[0.25em] text-slate-400">Workspace</p>
        <div className="space-y-2">
          {items.map(({ to, label, icon: Icon }) => (
            <NavLink
              key={to}
              to={to}
              className={({ isActive }) =>
                `flex items-center gap-3 rounded-2xl px-3 py-3 text-sm transition ${
                  isActive ? "bg-cyan-400 text-slate-950" : "text-slate-300 hover:bg-white/5 hover:text-white"
                }`
              }
            >
              <Icon className="h-4 w-4" />
              {label}
            </NavLink>
          ))}
        </div>
      </div>
    </aside>
  );
}
