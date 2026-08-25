# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 421
- HTTP: 108 alive / 62 gold
- HTTPS: 91 alive / 22 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 206 alive / 176 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35916
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
