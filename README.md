# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 418
- HTTP: 88 alive / 61 gold
- HTTPS: 36 alive / 25 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47091
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
