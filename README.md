# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 425
- HTTP: 103 alive / 66 gold
- HTTPS: 105 alive / 21 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 218 alive / 177 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35888
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
