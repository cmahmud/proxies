# SyndProxy private pool

## Current pool

- Alive now: 798
- Gold now: 385
- HTTP: 240 alive / 79 gold
- HTTPS: 123 alive / 15 gold
- SOCKS4: 225 alive / 152 gold
- SOCKS5: 210 alive / 139 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25468
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
