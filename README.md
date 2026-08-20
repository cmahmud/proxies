# SyndProxy private pool

## Current pool

- Alive now: 698
- Gold now: 363
- HTTP: 178 alive / 66 gold
- HTTPS: 141 alive / 21 gold
- SOCKS4: 189 alive / 135 gold
- SOCKS5: 190 alive / 141 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26682
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
