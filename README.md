# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 397
- HTTP: 77 alive / 60 gold
- HTTPS: 57 alive / 17 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42823
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
