# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 429
- HTTP: 139 alive / 71 gold
- HTTPS: 78 alive / 21 gold
- SOCKS4: 187 alive / 161 gold
- SOCKS5: 201 alive / 176 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36023
- Ever gold: 1264

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
