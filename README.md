# SyndProxy private pool

## Current pool

- Alive now: 711
- Gold now: 363
- HTTP: 185 alive / 70 gold
- HTTPS: 138 alive / 18 gold
- SOCKS4: 185 alive / 135 gold
- SOCKS5: 203 alive / 140 gold

## Historical pool

- Discovered: 149498
- Ever alive: 26691
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
