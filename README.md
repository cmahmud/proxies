# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 420
- HTTP: 99 alive / 65 gold
- HTTPS: 66 alive / 26 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47057
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
