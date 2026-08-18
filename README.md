# SyndProxy private pool

## Current pool

- Alive now: 648
- Gold now: 205
- HTTP: 148 alive / 23 gold
- HTTPS: 102 alive / 9 gold
- SOCKS4: 188 alive / 92 gold
- SOCKS5: 210 alive / 81 gold

## Historical pool

- Discovered: 89709
- Ever alive: 8000
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
