# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 340
- HTTP: 319 alive / 64 gold
- HTTPS: 196 alive / 14 gold
- SOCKS4: 242 alive / 144 gold
- SOCKS5: 205 alive / 118 gold

## Historical pool

- Discovered: 109959
- Ever alive: 15367
- Ever gold: 495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
