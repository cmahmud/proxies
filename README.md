# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 417
- HTTP: 86 alive / 64 gold
- HTTPS: 94 alive / 23 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35641
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
