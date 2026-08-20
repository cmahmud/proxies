# SyndProxy private pool

## Current pool

- Alive now: 643
- Gold now: 379
- HTTP: 169 alive / 74 gold
- HTTPS: 88 alive / 18 gold
- SOCKS4: 197 alive / 143 gold
- SOCKS5: 189 alive / 144 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25647
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
