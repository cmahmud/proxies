# SyndProxy private pool

## Current pool

- Alive now: 749
- Gold now: 397
- HTTP: 227 alive / 91 gold
- HTTPS: 114 alive / 25 gold
- SOCKS4: 177 alive / 123 gold
- SOCKS5: 231 alive / 158 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29479
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
