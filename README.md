# SyndProxy private pool

## Current pool

- Alive now: 1109
- Gold now: 399
- HTTP: 338 alive / 73 gold
- HTTPS: 238 alive / 12 gold
- SOCKS4: 259 alive / 153 gold
- SOCKS5: 274 alive / 161 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20608
- Ever gold: 869

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
