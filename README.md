# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 407
- HTTP: 255 alive / 96 gold
- HTTPS: 181 alive / 29 gold
- SOCKS4: 187 alive / 123 gold
- SOCKS5: 246 alive / 159 gold

## Historical pool

- Discovered: 167131
- Ever alive: 32550
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
