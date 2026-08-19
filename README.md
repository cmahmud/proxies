# SyndProxy private pool

## Current pool

- Alive now: 1102
- Gold now: 344
- HTTP: 426 alive / 65 gold
- HTTPS: 213 alive / 12 gold
- SOCKS4: 242 alive / 141 gold
- SOCKS5: 221 alive / 126 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20243
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
