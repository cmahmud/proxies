# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 281
- HTTP: 288 alive / 29 gold
- HTTPS: 160 alive / 5 gold
- SOCKS4: 241 alive / 137 gold
- SOCKS5: 215 alive / 110 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12384
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
