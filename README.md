# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 403
- HTTP: 97 alive / 70 gold
- HTTPS: 96 alive / 18 gold
- SOCKS4: 160 alive / 154 gold
- SOCKS5: 178 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43199
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
