# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 423
- HTTP: 106 alive / 72 gold
- HTTPS: 72 alive / 21 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44419
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
