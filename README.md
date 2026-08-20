# SyndProxy private pool

## Current pool

- Alive now: 1487
- Gold now: 587
- HTTP: 598 alive / 205 gold
- HTTPS: 439 alive / 96 gold
- SOCKS4: 223 alive / 150 gold
- SOCKS5: 227 alive / 136 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22839
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
