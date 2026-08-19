# SyndProxy private pool

## Current pool

- Alive now: 1082
- Gold now: 461
- HTTP: 361 alive / 122 gold
- HTTPS: 245 alive / 72 gold
- SOCKS4: 233 alive / 137 gold
- SOCKS5: 243 alive / 130 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16780
- Ever gold: 623

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
