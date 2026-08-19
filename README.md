# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 504
- HTTP: 328 alive / 159 gold
- HTTPS: 254 alive / 89 gold
- SOCKS4: 195 alive / 141 gold
- SOCKS5: 185 alive / 115 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18396
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
