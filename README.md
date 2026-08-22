# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 390
- HTTP: 330 alive / 89 gold
- HTTPS: 233 alive / 33 gold
- SOCKS4: 213 alive / 137 gold
- SOCKS5: 235 alive / 131 gold

## Historical pool

- Discovered: 161987
- Ever alive: 31289
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
