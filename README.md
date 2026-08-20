# SyndProxy private pool

## Current pool

- Alive now: 649
- Gold now: 330
- HTTP: 179 alive / 64 gold
- HTTPS: 122 alive / 17 gold
- SOCKS4: 165 alive / 123 gold
- SOCKS5: 183 alive / 126 gold

## Historical pool

- Discovered: 146668
- Ever alive: 25755
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
