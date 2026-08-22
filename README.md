# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 388
- HTTP: 198 alive / 91 gold
- HTTPS: 149 alive / 26 gold
- SOCKS4: 207 alive / 139 gold
- SOCKS5: 206 alive / 132 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31603
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
