# SyndProxy private pool

## Current pool

- Alive now: 756
- Gold now: 266
- HTTP: 211 alive / 32 gold
- HTTPS: 145 alive / 4 gold
- SOCKS4: 211 alive / 132 gold
- SOCKS5: 189 alive / 98 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10666
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
