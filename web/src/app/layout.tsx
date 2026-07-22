import type { Metadata } from 'next';
import { Barlow_Condensed } from 'next/font/google';
import './globals.css';

const barlowCondensed = Barlow_Condensed({
  variable: '--font-barlow-condensed',
  weight: ['400', '700'],
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
      className={`${barlowCondensed.variable} h-full antialiased`}
    >
      <body>{children}</body>
    </html>
  );
}
