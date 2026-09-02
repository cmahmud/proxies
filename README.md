# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 441
- HTTP: 95 alive / 73 gold
- HTTPS: 98 alive / 30 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47443
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
