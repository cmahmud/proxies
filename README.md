# SyndProxy private pool

## Current pool

- Alive now: 955
- Gold now: 341
- HTTP: 321 alive / 64 gold
- HTTPS: 193 alive / 14 gold
- SOCKS4: 236 alive / 144 gold
- SOCKS5: 205 alive / 119 gold

## Historical pool

- Discovered: 109959
- Ever alive: 15383
- Ever gold: 495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
