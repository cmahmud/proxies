# SyndProxy private pool

## Current pool

- Alive now: 729
- Gold now: 388
- HTTP: 205 alive / 70 gold
- HTTPS: 122 alive / 15 gold
- SOCKS4: 186 alive / 144 gold
- SOCKS5: 216 alive / 159 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25659
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
