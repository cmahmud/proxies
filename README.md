# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 428
- HTTP: 121 alive / 79 gold
- HTTPS: 68 alive / 24 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 207 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44337
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
