# SyndProxy private pool

## Current pool

- Alive now: 1640
- Gold now: 653
- HTTP: 637 alive / 218 gold
- HTTPS: 521 alive / 110 gold
- SOCKS4: 227 alive / 157 gold
- SOCKS5: 255 alive / 168 gold

## Historical pool

- Discovered: 141223
- Ever alive: 23940
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
