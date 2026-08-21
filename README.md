# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 368
- HTTP: 384 alive / 77 gold
- HTTPS: 277 alive / 25 gold
- SOCKS4: 181 alive / 115 gold
- SOCKS5: 246 alive / 151 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29915
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
