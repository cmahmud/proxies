# SyndProxy private pool

## Current pool

- Alive now: 711
- Gold now: 383
- HTTP: 178 alive / 68 gold
- HTTPS: 134 alive / 18 gold
- SOCKS4: 189 alive / 137 gold
- SOCKS5: 210 alive / 160 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25675
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
