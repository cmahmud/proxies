# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 475
- HTTP: 138 alive / 98 gold
- HTTPS: 119 alive / 38 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 201 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44887
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
