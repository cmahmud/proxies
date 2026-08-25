# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 417
- HTTP: 101 alive / 63 gold
- HTTPS: 82 alive / 23 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 194 alive / 170 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35795
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
