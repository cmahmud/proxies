# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 406
- HTTP: 108 alive / 64 gold
- HTTPS: 85 alive / 13 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37998
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
