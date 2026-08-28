# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 391
- HTTP: 93 alive / 68 gold
- HTTPS: 80 alive / 11 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 171 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43184
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
