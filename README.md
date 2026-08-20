# SyndProxy private pool

## Current pool

- Alive now: 1780
- Gold now: 643
- HTTP: 712 alive / 219 gold
- HTTPS: 520 alive / 117 gold
- SOCKS4: 217 alive / 147 gold
- SOCKS5: 331 alive / 160 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24201
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
