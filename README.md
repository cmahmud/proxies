# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 399
- HTTP: 87 alive / 68 gold
- HTTPS: 77 alive / 15 gold
- SOCKS4: 159 alive / 154 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43234
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
