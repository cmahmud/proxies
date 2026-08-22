# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 393
- HTTP: 261 alive / 87 gold
- HTTPS: 193 alive / 25 gold
- SOCKS4: 215 alive / 124 gold
- SOCKS5: 255 alive / 157 gold

## Historical pool

- Discovered: 164912
- Ever alive: 32131
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
