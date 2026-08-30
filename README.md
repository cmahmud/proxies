# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 419
- HTTP: 108 alive / 71 gold
- HTTPS: 67 alive / 22 gold
- SOCKS4: 163 alive / 161 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44382
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
