# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 324
- HTTP: 276 alive / 57 gold
- HTTPS: 158 alive / 15 gold
- SOCKS4: 196 alive / 125 gold
- SOCKS5: 192 alive / 127 gold

## Historical pool

- Discovered: 127417
- Ever alive: 19985
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
