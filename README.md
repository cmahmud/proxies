# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 537
- HTTP: 360 alive / 164 gold
- HTTPS: 238 alive / 92 gold
- SOCKS4: 215 alive / 133 gold
- SOCKS5: 217 alive / 148 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18731
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
