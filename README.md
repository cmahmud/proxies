# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 407
- HTTP: 352 alive / 91 gold
- HTTPS: 215 alive / 28 gold
- SOCKS4: 232 alive / 133 gold
- SOCKS5: 253 alive / 155 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32424
- Ever gold: 1180

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
