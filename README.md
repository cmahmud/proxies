# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 422
- HTTP: 97 alive / 65 gold
- HTTPS: 61 alive / 27 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47061
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
