# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 428
- HTTP: 117 alive / 65 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 207 alive / 178 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35932
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
