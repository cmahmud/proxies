# SyndProxy private pool

## Current pool

- Alive now: 1017
- Gold now: 431
- HTTP: 304 alive / 95 gold
- HTTPS: 175 alive / 24 gold
- SOCKS4: 253 alive / 147 gold
- SOCKS5: 285 alive / 165 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28162
- Ever gold: 1107

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
