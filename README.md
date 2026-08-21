# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 378
- HTTP: 238 alive / 80 gold
- HTTPS: 149 alive / 23 gold
- SOCKS4: 217 alive / 139 gold
- SOCKS5: 223 alive / 136 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29365
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
