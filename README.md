# SyndProxy private pool

## Current pool

- Alive now: 730
- Gold now: 377
- HTTP: 195 alive / 75 gold
- HTTPS: 129 alive / 21 gold
- SOCKS4: 209 alive / 141 gold
- SOCKS5: 197 alive / 140 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25633
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
