# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 424
- HTTP: 101 alive / 64 gold
- HTTPS: 103 alive / 26 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 196 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35821
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
