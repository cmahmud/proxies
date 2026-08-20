# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 403
- HTTP: 327 alive / 89 gold
- HTTPS: 229 alive / 27 gold
- SOCKS4: 191 alive / 133 gold
- SOCKS5: 220 alive / 154 gold

## Historical pool

- Discovered: 144731
- Ever alive: 24932
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
