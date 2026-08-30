# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 423
- HTTP: 135 alive / 82 gold
- HTTPS: 68 alive / 31 gold
- SOCKS4: 160 alive / 150 gold
- SOCKS5: 258 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43881
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
