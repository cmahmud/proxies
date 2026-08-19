# SyndProxy private pool

## Current pool

- Alive now: 1194
- Gold now: 396
- HTTP: 391 alive / 88 gold
- HTTPS: 304 alive / 15 gold
- SOCKS4: 240 alive / 130 gold
- SOCKS5: 259 alive / 163 gold

## Historical pool

- Discovered: 131856
- Ever alive: 21333
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
