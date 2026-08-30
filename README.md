# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 441
- HTTP: 114 alive / 82 gold
- HTTPS: 58 alive / 26 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43691
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
