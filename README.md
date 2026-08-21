# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 404
- HTTP: 295 alive / 92 gold
- HTTPS: 215 alive / 20 gold
- SOCKS4: 215 alive / 151 gold
- SOCKS5: 246 alive / 141 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29256
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
