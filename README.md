# SyndProxy private pool

## Current pool

- Alive now: 868
- Gold now: 405
- HTTP: 200 alive / 90 gold
- HTTPS: 198 alive / 22 gold
- SOCKS4: 204 alive / 127 gold
- SOCKS5: 266 alive / 166 gold

## Historical pool

- Discovered: 164909
- Ever alive: 32128
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
