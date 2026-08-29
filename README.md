# SyndProxy validated proxy pool

## Current pool

- Alive now: 373
- Gold now: 332
- HTTP: 47 alive / 31 gold
- HTTPS: 3 alive / 0 gold
- SOCKS4: 158 alive / 149 gold
- SOCKS5: 165 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43605
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
