# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 358
- HTTP: 255 alive / 99 gold
- HTTPS: 164 alive / 22 gold
- SOCKS4: 186 alive / 131 gold
- SOCKS5: 199 alive / 106 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28952
- Ever gold: 1117

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
