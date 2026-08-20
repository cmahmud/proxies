# SyndProxy private pool

## Current pool

- Alive now: 1091
- Gold now: 418
- HTTP: 318 alive / 94 gold
- HTTPS: 264 alive / 27 gold
- SOCKS4: 246 alive / 150 gold
- SOCKS5: 263 alive / 147 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25196
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
