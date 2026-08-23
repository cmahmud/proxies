# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 217
- HTTP: 145 alive / 36 gold
- HTTPS: 82 alive / 7 gold
- SOCKS4: 170 alive / 85 gold
- SOCKS5: 185 alive / 89 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32783
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
