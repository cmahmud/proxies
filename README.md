# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 420
- HTTP: 103 alive / 61 gold
- HTTPS: 94 alive / 21 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 216 alive / 177 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35904
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
