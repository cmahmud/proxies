# SyndProxy private pool

## Current pool

- Alive now: 696
- Gold now: 388
- HTTP: 173 alive / 72 gold
- HTTPS: 129 alive / 18 gold
- SOCKS4: 186 alive / 137 gold
- SOCKS5: 208 alive / 161 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25674
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
