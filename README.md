# SyndProxy private pool

## Current pool

- Alive now: 829
- Gold now: 356
- HTTP: 249 alive / 80 gold
- HTTPS: 180 alive / 27 gold
- SOCKS4: 186 alive / 118 gold
- SOCKS5: 214 alive / 131 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29775
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
