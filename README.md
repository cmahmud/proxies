# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 455
- HTTP: 127 alive / 86 gold
- HTTPS: 135 alive / 32 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46814
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
