# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 401
- HTTP: 113 alive / 65 gold
- HTTPS: 42 alive / 13 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33656
- Ever gold: 1246

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
