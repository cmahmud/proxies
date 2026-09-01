# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 423
- HTTP: 80 alive / 67 gold
- HTTPS: 83 alive / 26 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 177 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47144
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
