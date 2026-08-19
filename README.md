# SyndProxy private pool

## Current pool

- Alive now: 1089
- Gold now: 510
- HTTP: 418 alive / 158 gold
- HTTPS: 277 alive / 108 gold
- SOCKS4: 201 alive / 116 gold
- SOCKS5: 193 alive / 128 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19836
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
