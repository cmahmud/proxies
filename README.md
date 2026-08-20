# SyndProxy private pool

## Current pool

- Alive now: 703
- Gold now: 382
- HTTP: 185 alive / 72 gold
- HTTPS: 124 alive / 15 gold
- SOCKS4: 181 alive / 137 gold
- SOCKS5: 213 alive / 158 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25672
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
