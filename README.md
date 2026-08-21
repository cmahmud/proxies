# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 409
- HTTP: 231 alive / 91 gold
- HTTPS: 159 alive / 23 gold
- SOCKS4: 206 alive / 144 gold
- SOCKS5: 237 alive / 151 gold

## Historical pool

- Discovered: 152160
- Ever alive: 27814
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
