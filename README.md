# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 404
- HTTP: 109 alive / 61 gold
- HTTPS: 75 alive / 18 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38666
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
