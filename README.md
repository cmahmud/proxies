# SyndProxy private pool

## Current pool

- Alive now: 803
- Gold now: 400
- HTTP: 229 alive / 87 gold
- HTTPS: 150 alive / 22 gold
- SOCKS4: 193 alive / 135 gold
- SOCKS5: 231 alive / 156 gold

## Historical pool

- Discovered: 151681
- Ever alive: 27685
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
