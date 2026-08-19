# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 468
- HTTP: 382 alive / 118 gold
- HTTPS: 241 alive / 73 gold
- SOCKS4: 233 alive / 137 gold
- SOCKS5: 228 alive / 140 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16576
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
