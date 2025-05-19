import { Card } from '@/components/ui/card'
import { cn } from '@/lib/utils'
import { motion } from 'framer-motion'

export function Features() {
    return (
        <section className="bg-zinc-50 py-16 md:py-32 dark:bg-transparent">
            <div className="mx-auto max-w-2xl px-6 lg:max-w-5xl">
                <div className="mx-auto grid gap-4 lg:grid-cols-2">
                    {[1, 2, 3].map((i) => (
                        <motion.div
                            key={i}
                            initial={{ opacity: 0, y: 40 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.6, delay: i * 0.15 }}
                        >
                            <FeatureCard />
                        </motion.div>
                    ))}
                </div>
            </div>
        </section>
    )
}

interface FeatureCardProps {
    className?: string
}

const FeatureCard = ({ className }: FeatureCardProps) => (
    <Card className={cn('group relative rounded-none shadow-zinc-950/5 min-h-[300px]', className)}>
        <CardDecorator />
        {/* İçerik şimdilik boş */}
    </Card>
)

const CardDecorator = () => (
    <>
        <span className="border-primary absolute -left-px -top-px block size-2 border-l-2 border-t-2"></span>
        <span className="border-primary absolute -right-px -top-px block size-2 border-r-2 border-t-2"></span>
        <span className="border-primary absolute -bottom-px -left-px block size-2 border-b-2 border-l-2"></span>
        <span className="border-primary absolute -bottom-px -right-px block size-2 border-b-2 border-r-2"></span>
    </>
) 