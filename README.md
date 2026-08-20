# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 391
- HTTP: 186 alive / 72 gold
- HTTPS: 149 alive / 16 gold
- SOCKS4: 215 alive / 154 gold
- SOCKS5: 216 alive / 149 gold

## Historical pool

- Discovered: 149502
- Ever alive: 26740
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
