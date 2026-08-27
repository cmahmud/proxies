# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 417
- HTTP: 111 alive / 70 gold
- HTTPS: 174 alive / 18 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40980
- Ever gold: 1314

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
