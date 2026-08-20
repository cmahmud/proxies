# SyndProxy private pool

## Current pool

- Alive now: 683
- Gold now: 375
- HTTP: 176 alive / 66 gold
- HTTPS: 99 alive / 16 gold
- SOCKS4: 199 alive / 136 gold
- SOCKS5: 209 alive / 157 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25675
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
