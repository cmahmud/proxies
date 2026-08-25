# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 423
- HTTP: 122 alive / 64 gold
- HTTPS: 94 alive / 21 gold
- SOCKS4: 196 alive / 161 gold
- SOCKS5: 226 alive / 177 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35884
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
