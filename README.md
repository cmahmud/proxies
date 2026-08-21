# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 417
- HTTP: 338 alive / 110 gold
- HTTPS: 193 alive / 28 gold
- SOCKS4: 206 alive / 131 gold
- SOCKS5: 230 alive / 148 gold

## Historical pool

- Discovered: 160212
- Ever alive: 30630
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
