# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 274
- HTTP: 314 alive / 36 gold
- HTTPS: 187 alive / 8 gold
- SOCKS4: 218 alive / 137 gold
- SOCKS5: 165 alive / 93 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13932
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
