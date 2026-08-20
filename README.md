# SyndProxy private pool

## Current pool

- Alive now: 625
- Gold now: 353
- HTTP: 147 alive / 64 gold
- HTTPS: 99 alive / 19 gold
- SOCKS4: 185 alive / 131 gold
- SOCKS5: 194 alive / 139 gold

## Historical pool

- Discovered: 147017
- Ever alive: 25759
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
