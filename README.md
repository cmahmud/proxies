# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 407
- HTTP: 96 alive / 61 gold
- HTTPS: 76 alive / 21 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37035
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
