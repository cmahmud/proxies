# SyndProxy private pool

## Current pool

- Alive now: 669
- Gold now: 363
- HTTP: 178 alive / 71 gold
- HTTPS: 110 alive / 21 gold
- SOCKS4: 180 alive / 130 gold
- SOCKS5: 201 alive / 141 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25577
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
