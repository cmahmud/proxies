# SyndProxy private pool

## Current pool

- Alive now: 1555
- Gold now: 611
- HTTP: 546 alive / 211 gold
- HTTPS: 443 alive / 117 gold
- SOCKS4: 221 alive / 147 gold
- SOCKS5: 345 alive / 136 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23690
- Ever gold: 954

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
