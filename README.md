# SyndProxy private pool

## Current pool

- Alive now: 757
- Gold now: 404
- HTTP: 191 alive / 87 gold
- HTTPS: 128 alive / 23 gold
- SOCKS4: 221 alive / 143 gold
- SOCKS5: 217 alive / 151 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27729
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
