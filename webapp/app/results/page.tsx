"use client";
import { BentoCard, BentoGrid } from "@/components/ui/bento-grid";
import { StarBorder } from "@/components/ui/star-border";
import { GradualSpacing } from "@/components/ui/gradual-spacing";
import Link from "next/link";
import dynamic from "next/dynamic";

const MetricsBarChart = dynamic(
  () => import("@/components/ui/metrics-bar-chart").then(mod => mod.MetricsBarChart),
  { ssr: false }
);

const mockResult = {
  label: "Gerçek",
  confidence: 0.815,
  imageUrl: "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80",
  metrics: {
    accuracy: 0.815,
    total: 200,
    precision: 0.80,
    recall: 0.82,
    f1: 0.81,
  },
};

const metricsData = [
  { name: "Precision", value: mockResult.metrics.precision * 100 },
  { name: "Recall", value: mockResult.metrics.recall * 100 },
  { name: "F1", value: mockResult.metrics.f1 * 100 },
];

const features = [
  // Sol üst: Sonuç
  {
    customContent: (
      <div className="flex flex-col items-center justify-center h-full w-full gap-4">
        <span className={`px-4 py-2 rounded-full text-lg font-bold ${mockResult.label === "Gerçek" ? "bg-green-500/20 text-green-600" : "bg-red-500/20 text-red-600"}`}>{`Sonuç: ${mockResult.label}`}</span>
        <span className="text-sm text-muted-foreground">Güven: %{(mockResult.confidence * 100).toFixed(2)}</span>
      </div>
    ),
    className: "lg:col-start-1 lg:col-end-2 lg:row-start-1 lg:row-end-3",
  },
  // Orta: Yüklenen görsel
  {
    customContent: (
      <div className="flex items-center justify-center h-full w-full">
        <img src={mockResult.imageUrl} alt="Yüklenen görsel" className="rounded-xl max-h-[80%] max-w-[80%] object-contain shadow-lg" />
      </div>
    ),
    className: "lg:row-start-1 lg:row-end-4 lg:col-start-2 lg:col-end-3",
  },
  // Sol alt: Back to chat butonu
  {
    customContent: (
      <StarBorder as={Link} href="/chat" className="w-full max-w-xs">
        Back to chat
      </StarBorder>
    ),
    className: "lg:col-start-1 lg:col-end-2 lg:row-start-3 lg:row-end-4",
  },
  // Sağ üst: Model metrikleri
  {
    customContent: (
      <div className="flex flex-col items-center justify-center h-full w-full gap-4">
        <div className="text-lg font-semibold">Model Doğruluk</div>
        <span className="px-3 py-1 rounded-full bg-muted text-foreground font-bold">%{(mockResult.metrics.accuracy * 100).toFixed(2)}</span>
        <div className="text-sm text-muted-foreground">Toplam test: {mockResult.metrics.total}</div>
      </div>
    ),
    className: "lg:col-start-3 lg:col-end-3 lg:row-start-1 lg:row-end-2",
  },
  // Sağ alt: Radar chart (çok büyük, açıklama sağ alt ve silik)
  {
    customContent: (
      <div className="relative flex flex-col items-center justify-center h-full w-full">
        <MetricsBarChart data={metricsData} height={600} />
        <div className="absolute bottom-4 right-4 opacity-60 text-xs text-right max-w-sm">
          <div><b>Precision:</b> Modelin &quot;fake&quot; olarak işaretlediği örneklerin gerçekten fake olma oranı.</div>
          <div><b>Recall:</b> Gerçekten fake olan örneklerin model tarafından doğru yakalanma oranı.</div>
          <div><b>F1:</b> Precision ve Recall&#39;un dengeli ortalaması (harmonik ortalama).</div>
        </div>
      </div>
    ),
    className: "lg:col-start-3 lg:col-end-3 lg:row-start-2 lg:row-end-4",
  },
];

export default function ResultsPage() {
  return (
    <div className="flex flex-col min-h-screen w-full items-center justify-center bg-background p-4">
      <div className="mb-8 mt-4 w-full flex justify-center">
        <GradualSpacing
          className="font-display text-center text-4xl font-bold -tracking-widest text-black dark:text-white md:text-7xl md:leading-[5rem]"
          text="Deepfake AI Sonuçları"
        />
      </div>
      <BentoGrid className="w-full h-full min-h-[600px] lg:grid-rows-3">
        {features.map((feature, i) => (
          <BentoCard key={i} {...feature} />
        ))}
      </BentoGrid>
    </div>
  );
} 