# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 426
- HTTP: 283 alive / 91 gold
- HTTPS: 208 alive / 26 gold
- SOCKS4: 220 alive / 150 gold
- SOCKS5: 265 alive / 159 gold

## Historical pool

- Discovered: 154722
- Ever alive: 29084
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
