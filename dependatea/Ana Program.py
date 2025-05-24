import argparse
from .api_client import fetch_dependencies
from .analyzer import calculate_rewards
from .visualizer import draw_graph

def main():
    parser = argparse.ArgumentParser(description="DependaTea: Bağımlılık Analiz Aracı")
    subparsers = parser.add_subparsers(dest="command")
    
    analyze_parser = subparsers.add_parser("analyze")
    analyze_parser.add_argument("package")
    
    rewards_parser = subparsers.add_parser("rewards")
    rewards_parser.add_argument("package")

    args = parser.parse_args()
    
    if args.command == "analyze":
        data = fetch_dependencies(args.package)
        draw_graph(data, f"{args.package}_graph.png")
        print(f"✅ Grafik oluşturuldu: {args.package}_graph.png")

    elif args.command == "rewards":
        data = fetch_dependencies(args.package)
        rewards = calculate_rewards(data)
        print("🔐 Token Ödülleri:")
        for contributor, amount in rewards.items():
            print(f"- {contributor}: {amount:.2f} TEA")

if __name__ == "__main__":
    main()