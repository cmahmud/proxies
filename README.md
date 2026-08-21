# SyndProxy private pool

## Current pool

- Alive now: 1303
- Gold now: 428
- HTTP: 506 alive / 95 gold
- HTTPS: 335 alive / 31 gold
- SOCKS4: 214 alive / 140 gold
- SOCKS5: 248 alive / 162 gold

## Historical pool

- Discovered: 159270
- Ever alive: 30388
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
