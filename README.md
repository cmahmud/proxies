# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 457
- HTTP: 116 alive / 89 gold
- HTTPS: 116 alive / 35 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45653
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
