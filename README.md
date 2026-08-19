# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 505
- HTTP: 347 alive / 159 gold
- HTTPS: 251 alive / 88 gold
- SOCKS4: 208 alive / 141 gold
- SOCKS5: 193 alive / 117 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18377
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
