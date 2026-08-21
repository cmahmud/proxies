# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 396
- HTTP: 258 alive / 88 gold
- HTTPS: 149 alive / 22 gold
- SOCKS4: 217 alive / 147 gold
- SOCKS5: 248 alive / 139 gold

## Historical pool

- Discovered: 155694
- Ever alive: 29227
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
