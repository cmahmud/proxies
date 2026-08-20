# SyndProxy private pool

## Current pool

- Alive now: 1517
- Gold now: 637
- HTTP: 571 alive / 235 gold
- HTTPS: 467 alive / 119 gold
- SOCKS4: 225 alive / 145 gold
- SOCKS5: 254 alive / 138 gold

## Historical pool

- Discovered: 142747
- Ever alive: 24642
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
