# SyndProxy private pool

## Current pool

- Alive now: 684
- Gold now: 388
- HTTP: 189 alive / 72 gold
- HTTPS: 113 alive / 18 gold
- SOCKS4: 185 alive / 146 gold
- SOCKS5: 197 alive / 152 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25681
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
