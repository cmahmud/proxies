# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 427
- HTTP: 100 alive / 78 gold
- HTTPS: 128 alive / 24 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42129
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
