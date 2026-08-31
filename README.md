# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 447
- HTTP: 127 alive / 82 gold
- HTTPS: 84 alive / 33 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 206 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45575
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
