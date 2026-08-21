# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 402
- HTTP: 280 alive / 93 gold
- HTTPS: 227 alive / 32 gold
- SOCKS4: 223 alive / 148 gold
- SOCKS5: 238 alive / 129 gold

## Historical pool

- Discovered: 161006
- Ever alive: 30995
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
