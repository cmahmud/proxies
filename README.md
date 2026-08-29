# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 371
- HTTP: 65 alive / 49 gold
- HTTPS: 64 alive / 11 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 171 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43511
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
