import Link from 'next/link';

export function Footer() {
  return (
    <footer className='text-center text-stone-400 uppercase'>
      <span>
        Desenvolvido por{' '}
        <Link
          className='text-orange-400'
          target='_blank'
          href='https://github.com/sergiodantasz'
        >
          Sérgio Dantas
        </Link>
      </span>
      <span className='relative -top-0.5 mx-1.5 text-xs'>•</span>
      <span>
        Disponível no{' '}
        <Link
          className='text-orange-400'
          target='_blank'
          href='https://github.com/sergiodantasz/nba-salary-predictor'
        >
          GitHub
        </Link>
      </span>
    </footer>
  );
}
