# SyndProxy private pool

## Current pool

- Alive now: 702
- Gold now: 382
- HTTP: 191 alive / 72 gold
- HTTPS: 107 alive / 18 gold
- SOCKS4: 202 alive / 148 gold
- SOCKS5: 202 alive / 144 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25624
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
