# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 418
- HTTP: 124 alive / 82 gold
- HTTPS: 63 alive / 28 gold
- SOCKS4: 160 alive / 149 gold
- SOCKS5: 165 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43698
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
