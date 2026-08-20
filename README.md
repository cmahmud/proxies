# SyndProxy private pool

## Current pool

- Alive now: 1503
- Gold now: 588
- HTTP: 553 alive / 200 gold
- HTTPS: 406 alive / 99 gold
- SOCKS4: 237 alive / 140 gold
- SOCKS5: 307 alive / 149 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23382
- Ever gold: 919

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
