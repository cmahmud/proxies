# SyndProxy private pool

## Current pool

- Alive now: 1190
- Gold now: 396
- HTTP: 395 alive / 88 gold
- HTTPS: 278 alive / 21 gold
- SOCKS4: 225 alive / 136 gold
- SOCKS5: 292 alive / 151 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22166
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
