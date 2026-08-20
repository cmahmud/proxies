# SyndProxy private pool

## Current pool

- Alive now: 1106
- Gold now: 428
- HTTP: 343 alive / 100 gold
- HTTPS: 262 alive / 27 gold
- SOCKS4: 246 alive / 151 gold
- SOCKS5: 255 alive / 150 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25192
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
