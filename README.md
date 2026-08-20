# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 369
- HTTP: 301 alive / 67 gold
- HTTPS: 203 alive / 19 gold
- SOCKS4: 214 alive / 143 gold
- SOCKS5: 233 alive / 140 gold

## Historical pool

- Discovered: 149502
- Ever alive: 26719
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
