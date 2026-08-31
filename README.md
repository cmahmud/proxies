# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 443
- HTTP: 119 alive / 82 gold
- HTTPS: 114 alive / 29 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45637
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
