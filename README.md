# SyndProxy private pool

## Current pool

- Alive now: 898
- Gold now: 416
- HTTP: 260 alive / 88 gold
- HTTPS: 169 alive / 24 gold
- SOCKS4: 214 alive / 145 gold
- SOCKS5: 255 alive / 159 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29070
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
