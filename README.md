# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 368
- HTTP: 169 alive / 75 gold
- HTTPS: 185 alive / 19 gold
- SOCKS4: 188 alive / 135 gold
- SOCKS5: 201 alive / 139 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26137
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
