# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 322
- HTTP: 297 alive / 36 gold
- HTTPS: 160 alive / 9 gold
- SOCKS4: 231 alive / 144 gold
- SOCKS5: 214 alive / 133 gold

## Historical pool

- Discovered: 103711
- Ever alive: 14057
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
