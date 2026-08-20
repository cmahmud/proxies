# SyndProxy private pool

## Current pool

- Alive now: 631
- Gold now: 358
- HTTP: 154 alive / 65 gold
- HTTPS: 107 alive / 22 gold
- SOCKS4: 178 alive / 131 gold
- SOCKS5: 192 alive / 140 gold

## Historical pool

- Discovered: 147017
- Ever alive: 25759
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
