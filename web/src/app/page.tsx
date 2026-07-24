'use client';

import { SeasonPicker } from '@/components/season-picker';
import { useState } from 'react';
import {
  ActivityIcon,
  CalendarDaysIcon,
  ShieldIcon,
  TargetIcon,
} from 'lucide-react';
import type { Season } from '@/types/season';

export default function Page() {
  const [season, setSeason] = useState<Season>(2026);

  return (
    <div className='flex flex-col gap-6 rounded-2xl border border-stone-700 bg-stone-900 p-6'>
      {/* Season */}
      <div className='flex flex-col gap-3'>
        <h4 className='flex items-center gap-2'>
          <CalendarDaysIcon
            className='text-orange-400'
            size={15}
          />
          <span className='text-sm font-medium tracking-widest text-stone-400'>
            TEMPORADA
          </span>
        </h4>
        <SeasonPicker
          value={season}
          onChange={setSeason}
        />
      </div>
      {/* Profile */}
      <div>
        <header className='mb-6'>
          <h4 className='flex items-center gap-2'>
            <ShieldIcon
              className='text-orange-400'
              size={24}
            />
            <span className='text-2xl font-bold text-stone-200'>PERFIL</span>
          </h4>
          <p className='text-sm font-medium tracking-widest text-stone-600'>
            POSIÇÃO E MINUTAGEM
          </p>
        </header>
        <div>Content</div>
      </div>
      {/* Shooting */}
      <div>
        <header className='mb-6'>
          <h4 className='flex items-center gap-2'>
            <TargetIcon
              className='text-orange-400'
              size={24}
            />
            <span className='text-2xl font-bold text-stone-200'>ARREMESSO</span>
          </h4>
          <p className='text-sm font-medium tracking-widest text-stone-600'>
            EFICIÊNCIA OFENSIVA NO PERÍMETRO E NA LINHA
          </p>
        </header>
        <div>Content</div>
      </div>
      {/* Impact */}
      <div>
        <header className='mb-6'>
          <h4 className='flex items-center gap-2'>
            <ActivityIcon
              className='text-orange-400'
              size={24}
            />
            <span className='text-2xl font-bold text-stone-200'>IMPACTO</span>
          </h4>
          <p className='text-sm font-medium tracking-widest text-stone-600'>
            CONTRIBUIÇÃO DEFENSIVA E DE POSSE
          </p>
        </header>
        <div>Content</div>
      </div>
    </div>
  );
}
