import Link from 'next/link';

export function Footer() {
  return (
    <footer className='text-center text-stone-400'>
      <span>
        DESENVOLVIDO POR{' '}
        <Link
          className='text-orange-400'
          target='_blank'
          href='https://github.com/sergiodantasz'
        >
          SÉRGIO DANTAS
        </Link>
      </span>
      <span className='relative -top-0.5 mx-1.5 text-xs'>•</span>
      <span>
        DISPONÍVEL NO{' '}
        <Link
          className='text-orange-400'
          target='_blank'
          href='https://github.com/sergiodantasz/nba-salary-predictor'
        >
          GITHUB
        </Link>
      </span>
    </footer>
  );
}
