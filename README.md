# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 438
- HTTP: 123 alive / 83 gold
- HTTPS: 80 alive / 27 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44293
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
