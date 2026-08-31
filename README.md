# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 446
- HTTP: 124 alive / 82 gold
- HTTPS: 82 alive / 33 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 204 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45575
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
