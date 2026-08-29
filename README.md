# SyndProxy validated proxy pool

## Current pool

- Alive now: 441
- Gold now: 346
- HTTP: 82 alive / 44 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 159 alive / 147 gold
- SOCKS5: 158 alive / 145 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43640
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
