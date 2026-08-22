# SyndProxy private pool

## Current pool

- Alive now: 797
- Gold now: 408
- HTTP: 212 alive / 81 gold
- HTTPS: 156 alive / 29 gold
- SOCKS4: 188 alive / 139 gold
- SOCKS5: 241 alive / 159 gold

## Historical pool

- Discovered: 162241
- Ever alive: 31413
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
