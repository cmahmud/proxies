# SyndProxy private pool

## Current pool

- Alive now: 839
- Gold now: 396
- HTTP: 218 alive / 97 gold
- HTTPS: 206 alive / 24 gold
- SOCKS4: 195 alive / 127 gold
- SOCKS5: 220 alive / 148 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31375
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
