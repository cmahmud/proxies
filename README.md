# SyndProxy private pool

## Current pool

- Alive now: 901
- Gold now: 386
- HTTP: 272 alive / 82 gold
- HTTPS: 219 alive / 22 gold
- SOCKS4: 201 alive / 135 gold
- SOCKS5: 209 alive / 147 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27279
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
