# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 383
- HTTP: 125 alive / 51 gold
- HTTPS: 44 alive / 12 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 196 alive / 162 gold

## Historical pool

- Discovered: 178284
- Ever alive: 33363
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
