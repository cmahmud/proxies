# SyndProxy private pool

## Current pool

- Alive now: 1110
- Gold now: 417
- HTTP: 467 alive / 90 gold
- HTTPS: 170 alive / 24 gold
- SOCKS4: 224 alive / 143 gold
- SOCKS5: 249 alive / 160 gold

## Historical pool

- Discovered: 156412
- Ever alive: 29422
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
