from src.agent import UltimateRerankedAgent

def main():
    bot = UltimateRerankedAgent(pdf_path='data/documents/attention.pdf')
    
    print("\nWelcome to ContextForge!")
    print("Commands: /history | /clear | /stats | /session <id> | /exit\n")
    
    while True:
        try:
            q = input(f"[{bot.session_id}] You: ").strip()
            
            if not q:
                continue
            elif q == "/exit":
                print("Goodbye!")
                bot.close_connection()
                break
            elif q == "/history":
                print(bot.show_history())
                continue
            elif q == "/clear":
                print(bot.clear_memory())
                continue
            elif q == "/stats":
                print(bot.show_stats())
                continue
            elif q.startswith("/session "):
                new_session = q.split(" ", 1)[1].strip()
                bot.set_session(new_session)
                print(f"Switched to: {new_session}")
                continue
            else:
                print("AI: ", end="", flush=True)
                response = bot.stream_query(q)
                print(response)
                print()
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            bot.close_connection()
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()