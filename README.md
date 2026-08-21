# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 378
- HTTP: 240 alive / 81 gold
- HTTPS: 151 alive / 23 gold
- SOCKS4: 219 alive / 137 gold
- SOCKS5: 223 alive / 137 gold

## Historical pool

- Discovered: 155799
- Ever alive: 29363
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
