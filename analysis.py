import random

def run_experiment(trials=10):
    results = []
    for i in range(trials):
        success = random.random() > 0.6
        results.append({'trial': i + 1, 'success': success})
        status = "SUCCESS" if success else "FAIL"
        print(f'Trial {i+1}: {status}')

    wins = sum(1 for r in results if r['success'])
    rate = wins / trials * 100
    print(f'\nResult: {wins}/{trials} ({rate:.1f}% success rate)')
    return results

if __name__ == '__main__':
    print('=== drclawlab experiment ===')
    run_experiment(10)
