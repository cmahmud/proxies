# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 393
- HTTP: 90 alive / 63 gold
- HTTPS: 72 alive / 14 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 171 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43410
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
