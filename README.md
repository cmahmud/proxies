# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 404
- HTTP: 85 alive / 58 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41644
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
