# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 383
- HTTP: 202 alive / 76 gold
- HTTPS: 128 alive / 20 gold
- SOCKS4: 228 alive / 146 gold
- SOCKS5: 202 alive / 141 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25492
- Ever gold: 1062

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
