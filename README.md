# SyndProxy private pool

## Current pool

- Alive now: 1488
- Gold now: 598
- HTTP: 568 alive / 208 gold
- HTTPS: 428 alive / 104 gold
- SOCKS4: 246 alive / 150 gold
- SOCKS5: 246 alive / 136 gold

## Historical pool

- Discovered: 140469
- Ever alive: 23732
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
