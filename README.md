# SyndProxy private pool

## Current pool

- Alive now: 958
- Gold now: 506
- HTTP: 316 alive / 161 gold
- HTTPS: 259 alive / 88 gold
- SOCKS4: 199 alive / 141 gold
- SOCKS5: 184 alive / 116 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18382
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
