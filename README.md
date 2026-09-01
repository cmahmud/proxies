# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 420
- HTTP: 80 alive / 66 gold
- HTTPS: 78 alive / 25 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 175 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47142
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
