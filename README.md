# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 470
- HTTP: 132 alive / 94 gold
- HTTPS: 116 alive / 36 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 192 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46350
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
