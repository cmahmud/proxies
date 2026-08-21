# SyndProxy private pool

## Current pool

- Alive now: 1152
- Gold now: 416
- HTTP: 424 alive / 111 gold
- HTTPS: 268 alive / 29 gold
- SOCKS4: 226 alive / 131 gold
- SOCKS5: 234 alive / 145 gold

## Historical pool

- Discovered: 160214
- Ever alive: 30668
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
