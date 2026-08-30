# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 428
- HTTP: 134 alive / 86 gold
- HTTPS: 92 alive / 32 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 198 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44026
- Ever gold: 1390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
