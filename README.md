# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 397
- HTTP: 103 alive / 66 gold
- HTTPS: 48 alive / 15 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 188 alive / 161 gold

## Historical pool

- Discovered: 175438
- Ever alive: 33159
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
