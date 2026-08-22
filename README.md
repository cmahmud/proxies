# SyndProxy private pool

## Current pool

- Alive now: 1067
- Gold now: 409
- HTTP: 338 alive / 83 gold
- HTTPS: 250 alive / 25 gold
- SOCKS4: 224 alive / 150 gold
- SOCKS5: 255 alive / 151 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32289
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
