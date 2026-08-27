# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 416
- HTTP: 97 alive / 71 gold
- HTTPS: 105 alive / 23 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41959
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
