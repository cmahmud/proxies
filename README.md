# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 397
- HTTP: 79 alive / 58 gold
- HTTPS: 63 alive / 16 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 174 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42821
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
