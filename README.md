# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 402
- HTTP: 292 alive / 91 gold
- HTTPS: 195 alive / 30 gold
- SOCKS4: 231 alive / 155 gold
- SOCKS5: 227 alive / 126 gold

## Historical pool

- Discovered: 160987
- Ever alive: 30871
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
