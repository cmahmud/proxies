# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 466
- HTTP: 146 alive / 94 gold
- HTTPS: 125 alive / 38 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46910
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
