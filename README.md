# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 389
- HTTP: 90 alive / 64 gold
- HTTPS: 77 alive / 12 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 167 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43438
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
