# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 289
- HTTP: 379 alive / 28 gold
- HTTPS: 169 alive / 6 gold
- SOCKS4: 241 alive / 130 gold
- SOCKS5: 242 alive / 125 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13121
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
