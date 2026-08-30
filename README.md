# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 441
- HTTP: 101 alive / 82 gold
- HTTPS: 43 alive / 26 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 179 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43685
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
