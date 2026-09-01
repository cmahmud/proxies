# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 423
- HTTP: 95 alive / 66 gold
- HTTPS: 68 alive / 27 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47057
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
