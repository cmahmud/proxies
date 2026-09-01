# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 407
- HTTP: 78 alive / 54 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47108
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
