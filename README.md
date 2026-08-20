# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 418
- HTTP: 212 alive / 85 gold
- HTTPS: 169 alive / 20 gold
- SOCKS4: 215 alive / 158 gold
- SOCKS5: 231 alive / 155 gold

## Historical pool

- Discovered: 151073
- Ever alive: 27496
- Ever gold: 1098

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
