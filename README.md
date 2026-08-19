# SyndProxy private pool

## Current pool

- Alive now: 1286
- Gold now: 472
- HTTP: 467 alive / 131 gold
- HTTPS: 340 alive / 75 gold
- SOCKS4: 224 alive / 120 gold
- SOCKS5: 255 alive / 146 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17273
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
