# SyndProxy private pool

## Current pool

- Alive now: 1538
- Gold now: 582
- HTTP: 632 alive / 224 gold
- HTTPS: 491 alive / 94 gold
- SOCKS4: 175 alive / 104 gold
- SOCKS5: 240 alive / 160 gold

## Historical pool

- Discovered: 143428
- Ever alive: 24733
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
