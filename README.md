# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 420
- HTTP: 81 alive / 66 gold
- HTTPS: 73 alive / 24 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 179 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47140
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
