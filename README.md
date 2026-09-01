# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 420
- HTTP: 93 alive / 63 gold
- HTTPS: 70 alive / 27 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47059
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
