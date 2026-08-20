# SyndProxy private pool

## Current pool

- Alive now: 1239
- Gold now: 437
- HTTP: 407 alive / 102 gold
- HTTPS: 314 alive / 31 gold
- SOCKS4: 255 alive / 151 gold
- SOCKS5: 263 alive / 153 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25166
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
