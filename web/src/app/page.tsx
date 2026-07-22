'use client';

import { SeasonPicker } from '@/components/season-picker';
import { useState } from 'react';
import { LuCalendarDays } from 'react-icons/lu';
import type { Season } from '@/types/season';

export default function Page() {
  const [season, setSeason] = useState<Season>(2026);

  return (
    <div className='rounded-xl border border-stone-700 bg-stone-900 p-6'>
      <div className='flex flex-col gap-3'>
        <h4 className='flex items-center gap-2'>
          <LuCalendarDays className='text-orange-400' />
          <span className='text-sm font-medium tracking-widest text-stone-400'>
            TEMPORADA
          </span>
        </h4>
        <SeasonPicker
          value={season}
          onChange={setSeason}
        />
      </div>
    </div>
  );
}
