# SyndProxy private pool

## Current pool

- Alive now: 775
- Gold now: 384
- HTTP: 240 alive / 80 gold
- HTTPS: 102 alive / 18 gold
- SOCKS4: 192 alive / 135 gold
- SOCKS5: 241 alive / 151 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29756
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
