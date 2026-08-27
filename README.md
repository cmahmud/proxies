# SyndProxy validated proxy pool

## Current pool

- Alive now: 670
- Gold now: 410
- HTTP: 126 alive / 63 gold
- HTTPS: 180 alive / 12 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40819
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
