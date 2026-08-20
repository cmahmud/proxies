# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 406
- HTTP: 197 alive / 81 gold
- HTTPS: 161 alive / 21 gold
- SOCKS4: 203 alive / 152 gold
- SOCKS5: 230 alive / 152 gold

## Historical pool

- Discovered: 151073
- Ever alive: 27496
- Ever gold: 1098

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
