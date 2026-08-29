# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 358
- HTTP: 83 alive / 55 gold
- HTTPS: 61 alive / 11 gold
- SOCKS4: 166 alive / 152 gold
- SOCKS5: 172 alive / 140 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43482
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
