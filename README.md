# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 436
- HTTP: 106 alive / 78 gold
- HTTPS: 59 alive / 26 gold
- SOCKS4: 192 alive / 170 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49095
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
