# SyndProxy private pool

## Current pool

- Alive now: 1086
- Gold now: 486
- HTTP: 390 alive / 137 gold
- HTTPS: 259 alive / 80 gold
- SOCKS4: 211 alive / 120 gold
- SOCKS5: 226 alive / 149 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17868
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
