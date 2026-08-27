# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 405
- HTTP: 100 alive / 64 gold
- HTTPS: 104 alive / 16 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41420
- Ever gold: 1328

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
