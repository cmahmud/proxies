# SyndProxy private pool

## Current pool

- Alive now: 977
- Gold now: 392
- HTTP: 296 alive / 82 gold
- HTTPS: 224 alive / 26 gold
- SOCKS4: 213 alive / 149 gold
- SOCKS5: 244 alive / 135 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32521
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
