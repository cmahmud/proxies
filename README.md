# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 402
- HTTP: 95 alive / 63 gold
- HTTPS: 93 alive / 12 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43048
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
