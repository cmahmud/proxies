# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 451
- HTTP: 126 alive / 82 gold
- HTTPS: 96 alive / 36 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46998
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
