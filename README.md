# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 447
- HTTP: 119 alive / 82 gold
- HTTPS: 73 alive / 33 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 204 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45575
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
