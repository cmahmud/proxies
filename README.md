# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 411
- HTTP: 114 alive / 68 gold
- HTTPS: 166 alive / 15 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40933
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
