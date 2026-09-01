# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 460
- HTTP: 148 alive / 93 gold
- HTTPS: 122 alive / 35 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46867
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
