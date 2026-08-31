# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 454
- HTTP: 134 alive / 87 gold
- HTTPS: 89 alive / 36 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45604
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
