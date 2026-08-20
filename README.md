# SyndProxy private pool

## Current pool

- Alive now: 695
- Gold now: 367
- HTTP: 170 alive / 71 gold
- HTTPS: 141 alive / 17 gold
- SOCKS4: 189 alive / 145 gold
- SOCKS5: 195 alive / 134 gold

## Historical pool

- Discovered: 147653
- Ever alive: 25885
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
