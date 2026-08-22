# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 409
- HTTP: 208 alive / 85 gold
- HTTPS: 153 alive / 27 gold
- SOCKS4: 200 alive / 139 gold
- SOCKS5: 219 alive / 158 gold

## Historical pool

- Discovered: 162443
- Ever alive: 31436
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
