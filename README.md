# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 403
- HTTP: 266 alive / 79 gold
- HTTPS: 160 alive / 26 gold
- SOCKS4: 220 alive / 145 gold
- SOCKS5: 238 alive / 153 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29587
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
