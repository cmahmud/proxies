# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 389
- HTTP: 218 alive / 82 gold
- HTTPS: 175 alive / 26 gold
- SOCKS4: 220 alive / 146 gold
- SOCKS5: 212 alive / 135 gold

## Historical pool

- Discovered: 163331
- Ever alive: 31866
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
