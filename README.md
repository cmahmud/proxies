# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 372
- HTTP: 82 alive / 57 gold
- HTTPS: 63 alive / 15 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 169 alive / 143 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43470
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
