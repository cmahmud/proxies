# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 394
- HTTP: 89 alive / 69 gold
- HTTPS: 88 alive / 9 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43211
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
