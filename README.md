# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 442
- HTTP: 119 alive / 82 gold
- HTTPS: 67 alive / 29 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44596
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
