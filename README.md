# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 504
- HTTP: 348 alive / 159 gold
- HTTPS: 257 alive / 88 gold
- SOCKS4: 209 alive / 141 gold
- SOCKS5: 192 alive / 116 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18382
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
