# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 421
- HTTP: 349 alive / 96 gold
- HTTPS: 257 alive / 25 gold
- SOCKS4: 237 alive / 150 gold
- SOCKS5: 245 alive / 150 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25166
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
