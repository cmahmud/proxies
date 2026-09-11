# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 352
- HTTP: 83 alive / 72 gold
- HTTPS: 51 alive / 29 gold
- SOCKS4: 127 alive / 75 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48585
- Ever gold: 1557

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
