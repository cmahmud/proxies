# SyndProxy private pool

## Current pool

- Alive now: 1105
- Gold now: 531
- HTTP: 397 alive / 158 gold
- HTTPS: 260 alive / 85 gold
- SOCKS4: 235 alive / 149 gold
- SOCKS5: 213 alive / 139 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18060
- Ever gold: 713

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
