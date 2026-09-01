# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 459
- HTTP: 132 alive / 86 gold
- HTTPS: 119 alive / 34 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 194 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46769
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
