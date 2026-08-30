# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 427
- HTTP: 106 alive / 71 gold
- HTTPS: 56 alive / 27 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44450
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
