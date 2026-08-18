# SyndProxy private pool

## Current pool

- Alive now: 874
- Gold now: 285
- HTTP: 264 alive / 27 gold
- HTTPS: 138 alive / 5 gold
- SOCKS4: 247 alive / 143 gold
- SOCKS5: 225 alive / 110 gold

## Historical pool

- Discovered: 99552
- Ever alive: 12361
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
