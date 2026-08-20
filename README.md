# SyndProxy private pool

## Current pool

- Alive now: 769
- Gold now: 400
- HTTP: 188 alive / 80 gold
- HTTPS: 148 alive / 26 gold
- SOCKS4: 220 alive / 151 gold
- SOCKS5: 213 alive / 143 gold

## Historical pool

- Discovered: 149525
- Ever alive: 27021
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
