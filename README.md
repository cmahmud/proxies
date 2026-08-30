# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 428
- HTTP: 101 alive / 75 gold
- HTTPS: 61 alive / 25 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44431
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
