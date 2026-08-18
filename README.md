# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 349
- HTTP: 311 alive / 50 gold
- HTTPS: 195 alive / 16 gold
- SOCKS4: 236 alive / 142 gold
- SOCKS5: 236 alive / 141 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14685
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
