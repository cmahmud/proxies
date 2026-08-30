# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 445
- HTTP: 108 alive / 83 gold
- HTTPS: 53 alive / 27 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43683
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
