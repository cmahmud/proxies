# SyndProxy private pool

## Current pool

- Alive now: 848
- Gold now: 403
- HTTP: 254 alive / 92 gold
- HTTPS: 132 alive / 20 gold
- SOCKS4: 218 alive / 151 gold
- SOCKS5: 244 alive / 140 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29245
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
