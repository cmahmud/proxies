# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 397
- HTTP: 83 alive / 57 gold
- HTTPS: 44 alive / 15 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42842
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
