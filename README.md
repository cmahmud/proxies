# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 402
- HTTP: 187 alive / 80 gold
- HTTPS: 161 alive / 20 gold
- SOCKS4: 204 alive / 150 gold
- SOCKS5: 226 alive / 152 gold

## Historical pool

- Discovered: 151073
- Ever alive: 27498
- Ever gold: 1098

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
