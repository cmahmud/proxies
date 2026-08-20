# SyndProxy private pool

## Current pool

- Alive now: 709
- Gold now: 385
- HTTP: 180 alive / 72 gold
- HTTPS: 128 alive / 17 gold
- SOCKS4: 190 alive / 137 gold
- SOCKS5: 211 alive / 159 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25674
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
