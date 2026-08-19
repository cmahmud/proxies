# SyndProxy private pool

## Current pool

- Alive now: 1361
- Gold now: 386
- HTTP: 485 alive / 94 gold
- HTTPS: 327 alive / 16 gold
- SOCKS4: 261 alive / 136 gold
- SOCKS5: 288 alive / 140 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21597
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
