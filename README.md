# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 470
- HTTP: 133 alive / 95 gold
- HTTPS: 124 alive / 38 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44885
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
