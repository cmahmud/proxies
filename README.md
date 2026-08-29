# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 379
- HTTP: 68 alive / 51 gold
- HTTPS: 61 alive / 10 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 170 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43520
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
