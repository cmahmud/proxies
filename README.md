# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 406
- HTTP: 251 alive / 88 gold
- HTTPS: 182 alive / 22 gold
- SOCKS4: 204 alive / 141 gold
- SOCKS5: 242 alive / 155 gold

## Historical pool

- Discovered: 151689
- Ever alive: 27799
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
