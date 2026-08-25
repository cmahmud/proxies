# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 407
- HTTP: 91 alive / 65 gold
- HTTPS: 75 alive / 20 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 176 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37674
- Ever gold: 1286

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
