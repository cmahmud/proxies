# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 428
- HTTP: 105 alive / 68 gold
- HTTPS: 91 alive / 23 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 203 alive / 177 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35978
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
