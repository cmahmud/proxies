# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 379
- HTTP: 238 alive / 82 gold
- HTTPS: 151 alive / 22 gold
- SOCKS4: 221 alive / 139 gold
- SOCKS5: 224 alive / 136 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29363
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
