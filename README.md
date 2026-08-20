# SyndProxy private pool

## Current pool

- Alive now: 731
- Gold now: 404
- HTTP: 165 alive / 76 gold
- HTTPS: 127 alive / 23 gold
- SOCKS4: 223 alive / 150 gold
- SOCKS5: 216 alive / 155 gold

## Historical pool

- Discovered: 151061
- Ever alive: 27336
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
