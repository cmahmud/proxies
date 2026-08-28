# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 404
- HTTP: 97 alive / 64 gold
- HTTPS: 101 alive / 14 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43050
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
