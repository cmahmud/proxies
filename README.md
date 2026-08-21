# SyndProxy private pool

## Current pool

- Alive now: 881
- Gold now: 405
- HTTP: 267 alive / 93 gold
- HTTPS: 155 alive / 21 gold
- SOCKS4: 216 alive / 152 gold
- SOCKS5: 243 alive / 139 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29232
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
