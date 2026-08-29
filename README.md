# SyndProxy validated proxy pool

## Current pool

- Alive now: 437
- Gold now: 356
- HTTP: 61 alive / 44 gold
- HTTPS: 43 alive / 4 gold
- SOCKS4: 162 alive / 158 gold
- SOCKS5: 171 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43540
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
