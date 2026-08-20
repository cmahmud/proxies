# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 376
- HTTP: 328 alive / 92 gold
- HTTPS: 233 alive / 21 gold
- SOCKS4: 220 alive / 130 gold
- SOCKS5: 248 alive / 133 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25070
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
