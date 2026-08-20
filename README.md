# SyndProxy private pool

## Current pool

- Alive now: 701
- Gold now: 388
- HTTP: 174 alive / 73 gold
- HTTPS: 127 alive / 18 gold
- SOCKS4: 193 alive / 137 gold
- SOCKS5: 207 alive / 160 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25675
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
