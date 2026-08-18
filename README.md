# SyndProxy private pool

## Current pool

- Alive now: 731
- Gold now: 269
- HTTP: 194 alive / 33 gold
- HTTPS: 100 alive / 3 gold
- SOCKS4: 226 alive / 132 gold
- SOCKS5: 211 alive / 101 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10668
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
