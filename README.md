# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 260
- HTTP: 293 alive / 29 gold
- HTTPS: 161 alive / 3 gold
- SOCKS4: 215 alive / 119 gold
- SOCKS5: 230 alive / 109 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12064
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
