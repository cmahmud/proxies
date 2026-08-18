# SyndProxy private pool

## Current pool

- Alive now: 810
- Gold now: 282
- HTTP: 243 alive / 31 gold
- HTTPS: 122 alive / 5 gold
- SOCKS4: 222 alive / 141 gold
- SOCKS5: 223 alive / 105 gold

## Historical pool

- Discovered: 99053
- Ever alive: 11117
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
