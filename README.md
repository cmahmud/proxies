# SyndProxy private pool

## Current pool

- Alive now: 1112
- Gold now: 521
- HTTP: 448 alive / 177 gold
- HTTPS: 254 alive / 100 gold
- SOCKS4: 210 alive / 114 gold
- SOCKS5: 200 alive / 130 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19404
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
