# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 393
- HTTP: 75 alive / 50 gold
- HTTPS: 59 alive / 19 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42767
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
