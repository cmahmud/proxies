# SyndProxy validated proxy pool

## Current pool

- Alive now: 390
- Gold now: 354
- HTTP: 47 alive / 38 gold
- HTTPS: 16 alive / 4 gold
- SOCKS4: 160 alive / 155 gold
- SOCKS5: 167 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43594
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
