# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 441
- HTTP: 99 alive / 70 gold
- HTTPS: 90 alive / 31 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47454
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
