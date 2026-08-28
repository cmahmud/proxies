# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 402
- HTTP: 81 alive / 58 gold
- HTTPS: 93 alive / 22 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 174 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42981
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
