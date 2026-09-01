# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 425
- HTTP: 93 alive / 67 gold
- HTTPS: 44 alive / 26 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
