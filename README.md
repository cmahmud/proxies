# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 472
- HTTP: 156 alive / 102 gold
- HTTPS: 134 alive / 36 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45148
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
