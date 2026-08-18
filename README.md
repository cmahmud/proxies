# SyndProxy private pool

## Current pool

- Alive now: 714
- Gold now: 263
- HTTP: 201 alive / 31 gold
- HTTPS: 111 alive / 3 gold
- SOCKS4: 213 alive / 132 gold
- SOCKS5: 189 alive / 97 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10668
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
