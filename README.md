# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 411
- HTTP: 83 alive / 65 gold
- HTTPS: 98 alive / 24 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 173 alive / 165 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47231
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
