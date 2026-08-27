# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 400
- HTTP: 102 alive / 60 gold
- HTTPS: 124 alive / 15 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41379
- Ever gold: 1326

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
