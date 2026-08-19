# SyndProxy private pool

## Current pool

- Alive now: 1098
- Gold now: 520
- HTTP: 388 alive / 161 gold
- HTTPS: 265 alive / 88 gold
- SOCKS4: 221 alive / 139 gold
- SOCKS5: 224 alive / 132 gold

## Historical pool

- Discovered: 119875
- Ever alive: 18520
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
