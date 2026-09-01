# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 409
- HTTP: 84 alive / 62 gold
- HTTPS: 91 alive / 22 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 174 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47203
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
