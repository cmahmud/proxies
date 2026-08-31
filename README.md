# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 438
- HTTP: 145 alive / 74 gold
- HTTPS: 101 alive / 30 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 208 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45395
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
