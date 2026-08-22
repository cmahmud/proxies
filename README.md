# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 407
- HTTP: 270 alive / 90 gold
- HTTPS: 204 alive / 24 gold
- SOCKS4: 231 alive / 129 gold
- SOCKS5: 267 alive / 164 gold

## Historical pool

- Discovered: 164910
- Ever alive: 32131
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
