# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 428
- HTTP: 100 alive / 73 gold
- HTTPS: 71 alive / 26 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44427
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
