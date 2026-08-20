# SyndProxy private pool

## Current pool

- Alive now: 706
- Gold now: 381
- HTTP: 166 alive / 67 gold
- HTTPS: 133 alive / 18 gold
- SOCKS4: 196 alive / 137 gold
- SOCKS5: 211 alive / 159 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25675
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
