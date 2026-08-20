# SyndProxy private pool

## Current pool

- Alive now: 626
- Gold now: 354
- HTTP: 148 alive / 63 gold
- HTTPS: 103 alive / 21 gold
- SOCKS4: 184 alive / 131 gold
- SOCKS5: 191 alive / 139 gold

## Historical pool

- Discovered: 147017
- Ever alive: 25759
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
