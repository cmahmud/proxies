# SyndProxy private pool

## Current pool

- Alive now: 1196
- Gold now: 440
- HTTP: 403 alive / 108 gold
- HTTPS: 321 alive / 30 gold
- SOCKS4: 217 alive / 152 gold
- SOCKS5: 255 alive / 150 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28558
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
