# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 445
- HTTP: 297 alive / 123 gold
- HTTPS: 225 alive / 46 gold
- SOCKS4: 226 alive / 141 gold
- SOCKS5: 241 alive / 135 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16782
- Ever gold: 623

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
