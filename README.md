# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 409
- HTTP: 309 alive / 94 gold
- HTTPS: 248 alive / 24 gold
- SOCKS4: 192 alive / 129 gold
- SOCKS5: 229 alive / 162 gold

## Historical pool

- Discovered: 144729
- Ever alive: 24912
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
