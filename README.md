# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 401
- HTTP: 82 alive / 57 gold
- HTTPS: 36 alive / 16 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42853
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
