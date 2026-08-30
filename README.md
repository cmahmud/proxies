# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 418
- HTTP: 138 alive / 78 gold
- HTTPS: 85 alive / 29 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 280 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43854
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
