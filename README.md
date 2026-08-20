# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 376
- HTTP: 197 alive / 77 gold
- HTTPS: 121 alive / 19 gold
- SOCKS4: 191 alive / 134 gold
- SOCKS5: 228 alive / 146 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25607
- Ever gold: 1069

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
