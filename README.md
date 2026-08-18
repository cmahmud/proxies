# SyndProxy private pool

## Current pool

- Alive now: 851
- Gold now: 257
- HTTP: 263 alive / 26 gold
- HTTPS: 149 alive / 3 gold
- SOCKS4: 215 alive / 118 gold
- SOCKS5: 224 alive / 110 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12059
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
