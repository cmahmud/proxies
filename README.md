# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 421
- HTTP: 94 alive / 65 gold
- HTTPS: 65 alive / 27 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47062
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
