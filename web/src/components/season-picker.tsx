import clsx from 'clsx';
import { SEASONS } from '@/data/seasons';
import { formatCurrency, formatSeasonLabel } from '@/utils/format';
import type { Season } from '@/types/season';

type Props = { value: Season; onChange: (season: Season) => void };

export function SeasonPicker({ value, onChange }: Props) {
  return (
    <div className='flex flex-wrap gap-1.5'>
      {SEASONS.map((s) => {
        const isActive = s.season === value;
        return (
          <button
            key={s.season}
            type='button'
            onClick={() => onChange(s.season)}
            className={clsx(
              'flex flex-1 flex-col rounded-lg border px-4 py-2',
              isActive
                ? 'border-orange-400 bg-orange-600/15'
                : 'border-stone-700 opacity-80'
            )}
          >
            <span className='text-lg font-bold'>
              {formatSeasonLabel(s.season)}
            </span>
            <span
              className={clsx(
                'text-sm',
                isActive ? 'text-orange-400' : 'text-stone-400'
              )}
            >
              {formatCurrency(s.cap)}
            </span>
          </button>
        );
      })}
    </div>
  );
}
