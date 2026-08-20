# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 393
- HTTP: 259 alive / 84 gold
- HTTPS: 253 alive / 22 gold
- SOCKS4: 193 alive / 132 gold
- SOCKS5: 207 alive / 155 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27240
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
