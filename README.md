# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 441
- HTTP: 119 alive / 86 gold
- HTTPS: 49 alive / 26 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43667
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
