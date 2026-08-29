# SyndProxy validated proxy pool

## Current pool

- Alive now: 439
- Gold now: 371
- HTTP: 62 alive / 46 gold
- HTTPS: 44 alive / 8 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 169 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43525
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
