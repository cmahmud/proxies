# SyndProxy private pool

## Current pool

- Alive now: 1092
- Gold now: 537
- HTTP: 451 alive / 181 gold
- HTTPS: 259 alive / 110 gold
- SOCKS4: 191 alive / 117 gold
- SOCKS5: 191 alive / 129 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19407
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
