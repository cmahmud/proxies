# SyndProxy private pool

## Current pool

- Alive now: 935
- Gold now: 416
- HTTP: 263 alive / 90 gold
- HTTPS: 198 alive / 22 gold
- SOCKS4: 216 alive / 144 gold
- SOCKS5: 258 alive / 160 gold

## Historical pool

- Discovered: 154720
- Ever alive: 29079
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
