# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 404
- HTTP: 110 alive / 71 gold
- HTTPS: 63 alive / 27 gold
- SOCKS4: 156 alive / 149 gold
- SOCKS5: 174 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43654
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
