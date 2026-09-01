# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 438
- HTTP: 113 alive / 76 gold
- HTTPS: 92 alive / 32 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47013
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
