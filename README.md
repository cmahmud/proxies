# SyndProxy validated proxy pool

## Current pool

- Alive now: 354
- Gold now: 201
- HTTP: 34 alive / 16 gold
- HTTPS: 0 alive / 0 gold
- SOCKS4: 158 alive / 94 gold
- SOCKS5: 162 alive / 91 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43613
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
