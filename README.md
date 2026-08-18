# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 276
- HTTP: 322 alive / 37 gold
- HTTPS: 191 alive / 9 gold
- SOCKS4: 211 alive / 138 gold
- SOCKS5: 159 alive / 92 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13932
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
