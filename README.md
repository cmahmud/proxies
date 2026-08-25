# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 415
- HTTP: 89 alive / 62 gold
- HTTPS: 82 alive / 21 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36094
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
