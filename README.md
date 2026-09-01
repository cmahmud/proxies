# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 414
- HTTP: 90 alive / 62 gold
- HTTPS: 46 alive / 21 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47086
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
