# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 380
- HTTP: 316 alive / 80 gold
- HTTPS: 219 alive / 25 gold
- SOCKS4: 197 alive / 123 gold
- SOCKS5: 237 alive / 152 gold

## Historical pool

- Discovered: 164975
- Ever alive: 32265
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
