# SyndProxy private pool

## Current pool

- Alive now: 653
- Gold now: 356
- HTTP: 178 alive / 69 gold
- HTTPS: 97 alive / 20 gold
- SOCKS4: 180 alive / 125 gold
- SOCKS5: 198 alive / 142 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25597
- Ever gold: 1067

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
