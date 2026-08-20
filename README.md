# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 380
- HTTP: 271 alive / 86 gold
- HTTPS: 204 alive / 26 gold
- SOCKS4: 193 alive / 126 gold
- SOCKS5: 211 alive / 142 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27286
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
