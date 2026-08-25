# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 428
- HTTP: 114 alive / 65 gold
- HTTPS: 93 alive / 24 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 209 alive / 178 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35937
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
