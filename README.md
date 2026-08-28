# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 395
- HTTP: 82 alive / 53 gold
- HTTPS: 44 alive / 16 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 174 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42839
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
