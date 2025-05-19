import { Sidebar, SidebarBody, SidebarLink } from "@/components/ui/sidebar";
import AnimatedAIChatDemo from "@/components/ui/animated-ai-chat";
import { Home, BarChart2, Settings } from "lucide-react";
import { TypingAnimation } from "@/components/ui/typing-animation";

const links = [
  {
    label: "Anasayfa",
    href: "/",
    icon: <Home className="h-5 w-5" />,
  },
  {
    label: "Sonuçlar",
    href: "/results",
    icon: <BarChart2 className="h-5 w-5" />,
  },
  {
    label: "Ayarlar",
    href: "/settings",
    icon: <Settings className="h-5 w-5" />,
  },
];

export default function ChatPage() {
  return (
    <div className="flex min-h-screen bg-zinc-950">
      <Sidebar>
        <SidebarBody className="h-screen bg-zinc-900 dark:bg-zinc-900 flex flex-col gap-2 pt-8 w-[220px] border-r border-zinc-800">
          <TypingAnimation text="Deepfake AI" className="text-2xl font-bold text-white mb-8" duration={80} />
          <div className="flex flex-col gap-2">
            {links.map((link, idx) => (
              <SidebarLink
                key={idx}
                link={link}
                className="rounded-lg px-3 py-2 hover:bg-zinc-800 transition-all duration-150"
              />
            ))}
          </div>
          <div className="mt-auto pb-8">
            <TypingAnimation text="Deepfake AI" className="text-base font-semibold text-zinc-400" duration={40} />
          </div>
        </SidebarBody>
      </Sidebar>
      <main className="flex-1">
        <AnimatedAIChatDemo />
      </main>
    </div>
  );
} 