# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 401
- HTTP: 84 alive / 60 gold
- HTTPS: 76 alive / 17 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 171 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42908
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
