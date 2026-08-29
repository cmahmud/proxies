# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 404
- HTTP: 104 alive / 70 gold
- HTTPS: 61 alive / 25 gold
- SOCKS4: 163 alive / 153 gold
- SOCKS5: 168 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43651
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
