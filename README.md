# SyndProxy private pool

## Current pool

- Alive now: 1134
- Gold now: 583
- HTTP: 410 alive / 172 gold
- HTTPS: 323 alive / 145 gold
- SOCKS4: 214 alive / 135 gold
- SOCKS5: 187 alive / 131 gold

## Historical pool

- Discovered: 127415
- Ever alive: 19960
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
