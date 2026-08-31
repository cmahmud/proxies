# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 411
- HTTP: 114 alive / 57 gold
- HTTPS: 70 alive / 22 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45518
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
