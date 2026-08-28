# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 399
- HTTP: 86 alive / 68 gold
- HTTPS: 89 alive / 14 gold
- SOCKS4: 157 alive / 154 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43234
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
