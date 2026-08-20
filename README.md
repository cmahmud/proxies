# SyndProxy private pool

## Current pool

- Alive now: 759
- Gold now: 383
- HTTP: 169 alive / 69 gold
- HTTPS: 149 alive / 15 gold
- SOCKS4: 228 alive / 145 gold
- SOCKS5: 213 alive / 154 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26277
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
