# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 425
- HTTP: 115 alive / 74 gold
- HTTPS: 67 alive / 26 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 199 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44344
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
