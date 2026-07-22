import type { Metadata } from 'next';
import { Barlow_Condensed } from 'next/font/google';
import './globals.css';
import { Footer } from '@/components/footer';
import { Header } from '@/components/header';

const barlowCondensed = Barlow_Condensed({
  variable: '--font-barlow-condensed',
  weight: ['400', '500', '700'],
  subsets: ['latin'],
});

export const metadata: Metadata = {
  title: 'NBA Salary Predictor',
  description: 'Predição de salário de jogadores da NBA.',
};

type Props = Readonly<{ children: React.ReactNode }>;

export default function Layout({ children }: Props) {
  return (
    <html
      lang='pt-br'
      className={`${barlowCondensed.variable} h-full bg-stone-950 text-stone-50 antialiased`}
    >
      <body className='h-full'>
        <div className='mx-auto flex h-full max-w-6xl flex-col gap-12 px-6 py-12'>
          <Header />
          <div className='mb-auto'>{children}</div>
          <Footer />
        </div>
      </body>
    </html>
  );
}
