# SyndProxy private pool

## Current pool

- Alive now: 934
- Gold now: 403
- HTTP: 302 alive / 90 gold
- HTTPS: 193 alive / 27 gold
- SOCKS4: 212 alive / 150 gold
- SOCKS5: 227 alive / 136 gold

## Historical pool

- Discovered: 165823
- Ever alive: 32341
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
