# SyndProxy private pool

## Current pool

- Alive now: 687
- Gold now: 384
- HTTP: 182 alive / 68 gold
- HTTPS: 111 alive / 17 gold
- SOCKS4: 189 alive / 145 gold
- SOCKS5: 205 alive / 154 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25679
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
