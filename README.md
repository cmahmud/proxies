# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 420
- HTTP: 106 alive / 71 gold
- HTTPS: 95 alive / 21 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38012
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
