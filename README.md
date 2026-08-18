# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 257
- HTTP: 280 alive / 26 gold
- HTTPS: 142 alive / 3 gold
- SOCKS4: 214 alive / 118 gold
- SOCKS5: 220 alive / 110 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12048
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
