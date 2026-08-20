# SyndProxy private pool

## Current pool

- Alive now: 679
- Gold now: 383
- HTTP: 171 alive / 68 gold
- HTTPS: 104 alive / 17 gold
- SOCKS4: 197 alive / 141 gold
- SOCKS5: 207 alive / 157 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25676
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
