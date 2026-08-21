# SyndProxy private pool

## Current pool

- Alive now: 838
- Gold now: 393
- HTTP: 238 alive / 90 gold
- HTTPS: 193 alive / 20 gold
- SOCKS4: 195 alive / 137 gold
- SOCKS5: 212 alive / 146 gold

## Historical pool

- Discovered: 152166
- Ever alive: 27875
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
