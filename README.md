# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 386
- HTTP: 79 alive / 56 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 168 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43490
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
