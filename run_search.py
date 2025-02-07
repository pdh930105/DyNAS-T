import argparse

from dynast.dynast_manager import DyNAS
from dynast.utils import log, set_logger


def main(args):

    agent = DyNAS(
        supernet=args.supernet,
        optimization_metrics=args.optimization_metrics,
        measurements=args.measurements,
        search_tactic=args.search_tactic,
        num_evals=args.num_evals,
        results_path=args.results_path,
        dataset_path=args.dataset_path,
        seed=args.seed,
        population=args.population,
        batch_size=args.batch_size,
        search_algo=args.search_algo,
        verbose=args.verbose,
        supernet_ckpt_path=args.supernet_ckpt_path,
        device=args.device,
    )

    results = agent.search()

    log.info(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--supernet',
        default='ofa_mbv3_d234_e346_k357_w1.0',
        type=str,
        help='Super-network',
        choices=[
            'ofa_resnet50',
            'ofa_mbv3_d234_e346_k357_w1.0',
            'ofa_mbv3_d234_e346_k357_w1.2',
            'ofa_proxyless_d234_e346_k357_w1.3',
            'transformer_lt_wmt_en_de',
        ],
    )
    parser.add_argument('--seed', default=42, type=int, help='Random Seed')
    # TODO(macsz) might be better to list allowed elements here (or in help message)
    parser.add_argument(
        '--optimization_metrics',
        default=['accuracy_top1', 'macs'],  # TODO*macsz) Consider just 'accuracy',
        # as it translates better for both image classification
        # and Transformer LT
        nargs='*',
        type=str,
        help='Metrics that will be optimized for during search.',
    )
    parser.add_argument(
        '--measurements',
        default=['accuracy_top1', 'macs', 'params', 'latency'],  # TODO(macsz) Ditto
        nargs='*',
        type=str,
        help='Measurements during search.',
    )
    parser.add_argument('-d', '--device', default='cpu', type=str, help='Target device to run measurements on.')
    parser.add_argument('--num_evals', default=250, type=int, help='Total number of evaluations during search.')
    parser.add_argument('--batch_size', default=1, type=int, help='Batch size for latency measurement calculation.')
    parser.add_argument('--population', default=50, type=int, help='Population size for each generation')
    parser.add_argument('--results_path', required=True, type=str, help='Path to store search results, csv format')
    parser.add_argument('--dataset_path', default='/datasets/imagenet-ilsvrc2012', type=str, help='')
    parser.add_argument('--supernet_ckpt_path', default=None, type=str, help='Path to supernet checkpoint.')

    parser.add_argument(
        '--search_tactic',
        default='linas',
        choices=['linas', 'evolutionary', 'random'],
        help='Search tactic, currently supports: ["linas", "evolutionary" , "random"]',
    )
    parser.add_argument(
        '--search_algo',
        default='nsga2',
        choices=['cmaes', 'nsga2', 'age', 'unsga3', 'ga', 'ctaea', 'moead'],
        help='Search algorithm, currently supports: ["cmaes", "nsga2", "age", "unsga3", "ga", "ctaea", "moead"]',
    )
    parser.add_argument('-v', '--verbose', action='store_true', help='Print more information.')

    args = parser.parse_args()

    set_logger()

    main(args)
