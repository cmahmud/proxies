# SyndProxy validated proxy pool

## Current pool

- Alive now: 362
- Gold now: 328
- HTTP: 40 alive / 26 gold
- HTTPS: 1 alive / 0 gold
- SOCKS4: 158 alive / 153 gold
- SOCKS5: 163 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43613
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
