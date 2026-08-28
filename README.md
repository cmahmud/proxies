# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 397
- HTTP: 72 alive / 53 gold
- HTTPS: 63 alive / 23 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 172 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42784
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
