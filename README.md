# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 428
- HTTP: 145 alive / 71 gold
- HTTPS: 75 alive / 20 gold
- SOCKS4: 185 alive / 161 gold
- SOCKS5: 204 alive / 176 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36023
- Ever gold: 1264

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
