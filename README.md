# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 450
- HTTP: 115 alive / 86 gold
- HTTPS: 78 alive / 32 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 199 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45575
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
