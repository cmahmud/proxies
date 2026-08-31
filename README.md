# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 436
- HTTP: 110 alive / 75 gold
- HTTPS: 80 alive / 28 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 202 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45463
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
