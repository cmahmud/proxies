# SyndProxy private pool

## Current pool

- Alive now: 687
- Gold now: 386
- HTTP: 185 alive / 70 gold
- HTTPS: 118 alive / 18 gold
- SOCKS4: 188 alive / 145 gold
- SOCKS5: 196 alive / 153 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25681
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
