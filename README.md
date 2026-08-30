# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 420
- HTTP: 113 alive / 69 gold
- HTTPS: 65 alive / 22 gold
- SOCKS4: 162 alive / 162 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44379
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
