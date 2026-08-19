# SyndProxy private pool

## Current pool

- Alive now: 1208
- Gold now: 496
- HTTP: 387 alive / 121 gold
- HTTPS: 280 alive / 71 gold
- SOCKS4: 248 alive / 154 gold
- SOCKS5: 293 alive / 150 gold

## Historical pool

- Discovered: 114412
- Ever alive: 17032
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
