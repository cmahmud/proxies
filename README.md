# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 423
- HTTP: 84 alive / 68 gold
- HTTPS: 86 alive / 25 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47172
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
