# SyndProxy validated proxy pool

## Current pool

- Alive now: 734
- Gold now: 198
- HTTP: 284 alive / 36 gold
- HTTPS: 49 alive / 6 gold
- SOCKS4: 211 alive / 68 gold
- SOCKS5: 190 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32771
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
