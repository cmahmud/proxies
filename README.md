# SyndProxy private pool

## Current pool

- Alive now: 1653
- Gold now: 636
- HTTP: 648 alive / 233 gold
- HTTPS: 538 alive / 119 gold
- SOCKS4: 207 alive / 138 gold
- SOCKS5: 260 alive / 146 gold

## Historical pool

- Discovered: 142740
- Ever alive: 24599
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
