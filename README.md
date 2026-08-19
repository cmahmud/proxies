# SyndProxy private pool

## Current pool

- Alive now: 1251
- Gold now: 388
- HTTP: 436 alive / 84 gold
- HTTPS: 309 alive / 12 gold
- SOCKS4: 228 alive / 130 gold
- SOCKS5: 278 alive / 162 gold

## Historical pool

- Discovered: 133919
- Ever alive: 21427
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
