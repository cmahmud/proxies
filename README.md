# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 390
- HTTP: 186 alive / 71 gold
- HTTPS: 154 alive / 15 gold
- SOCKS4: 188 alive / 144 gold
- SOCKS5: 215 alive / 160 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25672
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
