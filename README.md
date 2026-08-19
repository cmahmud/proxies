# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 372
- HTTP: 310 alive / 65 gold
- HTTPS: 223 alive / 19 gold
- SOCKS4: 227 alive / 127 gold
- SOCKS5: 233 alive / 161 gold

## Historical pool

- Discovered: 109991
- Ever alive: 15669
- Ever gold: 499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
