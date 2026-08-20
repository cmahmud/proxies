# SyndProxy private pool

## Current pool

- Alive now: 1459
- Gold now: 605
- HTTP: 502 alive / 202 gold
- HTTPS: 418 alive / 99 gold
- SOCKS4: 244 alive / 145 gold
- SOCKS5: 295 alive / 159 gold

## Historical pool

- Discovered: 140459
- Ever alive: 23592
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
