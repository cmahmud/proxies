# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 433
- HTTP: 114 alive / 78 gold
- HTTPS: 68 alive / 27 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44304
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
