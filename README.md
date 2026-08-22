# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 397
- HTTP: 310 alive / 90 gold
- HTTPS: 247 alive / 24 gold
- SOCKS4: 227 alive / 137 gold
- SOCKS5: 251 alive / 146 gold

## Historical pool

- Discovered: 164248
- Ever alive: 32108
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
