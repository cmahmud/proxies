# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 376
- HTTP: 301 alive / 70 gold
- HTTPS: 208 alive / 21 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 227 alive / 143 gold

## Historical pool

- Discovered: 149502
- Ever alive: 26720
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
