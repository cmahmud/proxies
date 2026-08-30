# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 426
- HTTP: 136 alive / 85 gold
- HTTPS: 89 alive / 32 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 196 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44028
- Ever gold: 1390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
