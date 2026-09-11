# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 433
- HTTP: 106 alive / 76 gold
- HTTPS: 53 alive / 27 gold
- SOCKS4: 195 alive / 165 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49112
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
