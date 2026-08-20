# SyndProxy private pool

## Current pool

- Alive now: 625
- Gold now: 356
- HTTP: 158 alive / 66 gold
- HTTPS: 107 alive / 20 gold
- SOCKS4: 173 alive / 131 gold
- SOCKS5: 187 alive / 139 gold

## Historical pool

- Discovered: 147017
- Ever alive: 25758
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
