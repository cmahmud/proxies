# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 405
- HTTP: 248 alive / 89 gold
- HTTPS: 184 alive / 22 gold
- SOCKS4: 210 alive / 141 gold
- SOCKS5: 241 alive / 153 gold

## Historical pool

- Discovered: 151902
- Ever alive: 27804
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
