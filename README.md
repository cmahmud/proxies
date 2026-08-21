# SyndProxy private pool

## Current pool

- Alive now: 1122
- Gold now: 412
- HTTP: 357 alive / 96 gold
- HTTPS: 289 alive / 37 gold
- SOCKS4: 244 alive / 146 gold
- SOCKS5: 232 alive / 133 gold

## Historical pool

- Discovered: 160998
- Ever alive: 30980
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
