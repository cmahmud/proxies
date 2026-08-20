# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 404
- HTTP: 218 alive / 74 gold
- HTTPS: 165 alive / 22 gold
- SOCKS4: 226 alive / 150 gold
- SOCKS5: 225 alive / 158 gold

## Historical pool

- Discovered: 151061
- Ever alive: 27374
- Ever gold: 1095

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
