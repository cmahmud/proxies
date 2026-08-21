# SyndProxy private pool

## Current pool

- Alive now: 815
- Gold now: 392
- HTTP: 225 alive / 89 gold
- HTTPS: 149 alive / 20 gold
- SOCKS4: 221 alive / 129 gold
- SOCKS5: 220 alive / 154 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27768
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
