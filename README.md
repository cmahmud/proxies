# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 288
- HTTP: 235 alive / 27 gold
- HTTPS: 144 alive / 5 gold
- SOCKS4: 244 alive / 146 gold
- SOCKS5: 220 alive / 110 gold

## Historical pool

- Discovered: 99929
- Ever alive: 12362
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
