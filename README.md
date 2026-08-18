# SyndProxy private pool

## Current pool

- Alive now: 940
- Gold now: 325
- HTTP: 285 alive / 35 gold
- HTTPS: 188 alive / 10 gold
- SOCKS4: 235 alive / 147 gold
- SOCKS5: 232 alive / 133 gold

## Historical pool

- Discovered: 106999
- Ever alive: 14205
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
