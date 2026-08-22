# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 393
- HTTP: 237 alive / 90 gold
- HTTPS: 177 alive / 27 gold
- SOCKS4: 193 alive / 140 gold
- SOCKS5: 210 alive / 136 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31619
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
