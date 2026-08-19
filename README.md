# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 488
- HTTP: 369 alive / 130 gold
- HTTPS: 242 alive / 84 gold
- SOCKS4: 193 alive / 121 gold
- SOCKS5: 235 alive / 153 gold

## Historical pool

- Discovered: 119650
- Ever alive: 17849
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
