# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 436
- HTTP: 108 alive / 74 gold
- HTTPS: 53 alive / 28 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 207 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45553
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
