# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 430
- HTTP: 121 alive / 73 gold
- HTTPS: 72 alive / 26 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45529
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
