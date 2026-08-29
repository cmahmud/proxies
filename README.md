# SyndProxy validated proxy pool

## Current pool

- Alive now: 322
- Gold now: 215
- HTTP: 29 alive / 15 gold
- HTTPS: 1 alive / 0 gold
- SOCKS4: 147 alive / 106 gold
- SOCKS5: 145 alive / 94 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43629
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
