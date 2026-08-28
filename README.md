# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 399
- HTTP: 108 alive / 69 gold
- HTTPS: 89 alive / 14 gold
- SOCKS4: 162 alive / 152 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43188
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
