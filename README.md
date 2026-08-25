# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 430
- HTTP: 125 alive / 76 gold
- HTTPS: 82 alive / 23 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34793
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
