# SyndProxy private pool

## Current pool

- Alive now: 1144
- Gold now: 499
- HTTP: 385 alive / 124 gold
- HTTPS: 264 alive / 75 gold
- SOCKS4: 229 alive / 149 gold
- SOCKS5: 266 alive / 151 gold

## Historical pool

- Discovered: 114412
- Ever alive: 17027
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
