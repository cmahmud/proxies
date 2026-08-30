# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 438
- HTTP: 114 alive / 81 gold
- HTTPS: 57 alive / 30 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44301
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
