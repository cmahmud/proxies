# SyndProxy private pool

## Current pool

- Alive now: 859
- Gold now: 260
- HTTP: 284 alive / 28 gold
- HTTPS: 133 alive / 3 gold
- SOCKS4: 222 alive / 119 gold
- SOCKS5: 220 alive / 110 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12045
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
