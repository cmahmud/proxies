# SyndProxy private pool

## Current pool

- Alive now: 1857
- Gold now: 695
- HTTP: 704 alive / 233 gold
- HTTPS: 597 alive / 144 gold
- SOCKS4: 223 alive / 153 gold
- SOCKS5: 333 alive / 165 gold

## Historical pool

- Discovered: 142714
- Ever alive: 24460
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
