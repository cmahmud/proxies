# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 403
- HTTP: 112 alive / 61 gold
- HTTPS: 66 alive / 16 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38359
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
