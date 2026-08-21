# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 406
- HTTP: 259 alive / 89 gold
- HTTPS: 151 alive / 21 gold
- SOCKS4: 209 alive / 138 gold
- SOCKS5: 225 alive / 158 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27641
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
