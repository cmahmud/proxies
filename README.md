# SyndProxy private pool

## Current pool

- Alive now: 1161
- Gold now: 570
- HTTP: 419 alive / 192 gold
- HTTPS: 273 alive / 95 gold
- SOCKS4: 240 alive / 146 gold
- SOCKS5: 229 alive / 137 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22864
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
