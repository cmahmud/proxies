# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 438
- HTTP: 109 alive / 79 gold
- HTTPS: 63 alive / 28 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44571
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
