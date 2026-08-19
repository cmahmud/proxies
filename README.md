# SyndProxy private pool

## Current pool

- Alive now: 1213
- Gold now: 460
- HTTP: 448 alive / 122 gold
- HTTPS: 317 alive / 72 gold
- SOCKS4: 227 alive / 138 gold
- SOCKS5: 221 alive / 128 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16732
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
