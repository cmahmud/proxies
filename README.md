# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 421
- HTTP: 85 alive / 68 gold
- HTTPS: 82 alive / 25 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47172
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
