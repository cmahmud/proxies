# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 431
- HTTP: 112 alive / 66 gold
- HTTPS: 85 alive / 25 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 204 alive / 179 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35940
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
