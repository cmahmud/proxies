# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 386
- HTTP: 348 alive / 78 gold
- HTTPS: 215 alive / 25 gold
- SOCKS4: 205 alive / 128 gold
- SOCKS5: 241 alive / 155 gold

## Historical pool

- Discovered: 166564
- Ever alive: 32407
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
