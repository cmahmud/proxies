# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 438
- HTTP: 104 alive / 82 gold
- HTTPS: 66 alive / 25 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 194 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44560
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
