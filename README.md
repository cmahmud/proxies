# SyndProxy private pool

## Current pool

- Alive now: 546
- Gold now: 215
- HTTP: 151 alive / 34 gold
- HTTPS: 91 alive / 12 gold
- SOCKS4: 151 alive / 99 gold
- SOCKS5: 153 alive / 70 gold

## Historical pool

- Discovered: 82965
- Ever alive: 5062
- Ever gold: 285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
