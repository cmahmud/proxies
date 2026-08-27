# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 402
- HTTP: 112 alive / 64 gold
- HTTPS: 161 alive / 10 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40942
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
