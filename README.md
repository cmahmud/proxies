# SyndProxy private pool

## Current pool

- Alive now: 898
- Gold now: 339
- HTTP: 314 alive / 63 gold
- HTTPS: 190 alive / 13 gold
- SOCKS4: 203 alive / 137 gold
- SOCKS5: 191 alive / 126 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20212
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
