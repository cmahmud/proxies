# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 326
- HTTP: 315 alive / 60 gold
- HTTPS: 181 alive / 9 gold
- SOCKS4: 219 alive / 126 gold
- SOCKS5: 209 alive / 131 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20126
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
