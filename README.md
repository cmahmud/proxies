# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 317
- HTTP: 298 alive / 55 gold
- HTTPS: 199 alive / 11 gold
- SOCKS4: 207 alive / 124 gold
- SOCKS5: 210 alive / 127 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20130
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
