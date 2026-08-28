# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 402
- HTTP: 100 alive / 68 gold
- HTTPS: 101 alive / 12 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 175 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43057
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
