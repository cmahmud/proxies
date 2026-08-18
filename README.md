# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 280
- HTTP: 381 alive / 24 gold
- HTTPS: 159 alive / 5 gold
- SOCKS4: 217 alive / 138 gold
- SOCKS5: 221 alive / 113 gold

## Historical pool

- Discovered: 102825
- Ever alive: 12927
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
