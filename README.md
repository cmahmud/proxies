# SyndProxy private pool

## Current pool

- Alive now: 705
- Gold now: 192
- HTTP: 255 alive / 22 gold
- HTTPS: 99 alive / 8 gold
- SOCKS4: 166 alive / 97 gold
- SOCKS5: 185 alive / 65 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8117
- Ever gold: 347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
