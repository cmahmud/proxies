# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 341
- HTTP: 323 alive / 63 gold
- HTTPS: 242 alive / 15 gold
- SOCKS4: 231 alive / 144 gold
- SOCKS5: 201 alive / 119 gold

## Historical pool

- Discovered: 109959
- Ever alive: 15383
- Ever gold: 495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
