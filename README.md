# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 427
- HTTP: 127 alive / 66 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 201 alive / 161 gold
- SOCKS5: 227 alive / 177 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35868
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
