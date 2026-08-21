# SyndProxy private pool

## Current pool

- Alive now: 1263
- Gold now: 396
- HTTP: 457 alive / 99 gold
- HTTPS: 328 alive / 27 gold
- SOCKS4: 223 alive / 127 gold
- SOCKS5: 255 alive / 143 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28100
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
