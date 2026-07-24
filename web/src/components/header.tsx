export function Header() {
  return (
    <header>
      <h1 className='mb-3 font-bold'>
        <span className='text-9xl text-orange-400'>NBA</span>
        <br />
        <span className='text-5xl'>
          SALARY{' '}
          <span
            className='text-transparent'
            style={{ WebkitTextStroke: '1px oklch(75% 0.183 55.934)' }}
          >
            PREDICTOR
          </span>
        </span>
      </h1>
      <p className='leading-5 text-stone-400'>
        Monte o perfil de desempenho ajustando as métricas da temporada e deixe
        o modelo estimar o salário anual do atleta na NBA.
      </p>
    </header>
  );
}
