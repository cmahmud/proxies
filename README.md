# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 431
- HTTP: 113 alive / 78 gold
- HTTPS: 67 alive / 26 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44304
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
