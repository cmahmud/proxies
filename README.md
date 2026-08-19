# SyndProxy private pool

## Current pool

- Alive now: 1099
- Gold now: 479
- HTTP: 398 alive / 131 gold
- HTTPS: 273 alive / 78 gold
- SOCKS4: 208 alive / 120 gold
- SOCKS5: 220 alive / 150 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17874
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
