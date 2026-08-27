# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 403
- HTTP: 89 alive / 56 gold
- HTTPS: 52 alive / 22 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41688
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
