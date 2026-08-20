# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 393
- HTTP: 296 alive / 97 gold
- HTTPS: 240 alive / 25 gold
- SOCKS4: 248 alive / 133 gold
- SOCKS5: 241 alive / 138 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25107
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
