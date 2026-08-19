# SyndProxy private pool

## Current pool

- Alive now: 923
- Gold now: 461
- HTTP: 293 alive / 117 gold
- HTTPS: 205 alive / 87 gold
- SOCKS4: 226 alive / 140 gold
- SOCKS5: 199 alive / 117 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17488
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
