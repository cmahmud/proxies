# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 373
- HTTP: 303 alive / 65 gold
- HTTPS: 247 alive / 19 gold
- SOCKS4: 203 alive / 128 gold
- SOCKS5: 250 alive / 161 gold

## Historical pool

- Discovered: 110439
- Ever alive: 15747
- Ever gold: 503

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
