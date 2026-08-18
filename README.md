# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 369
- HTTP: 307 alive / 60 gold
- HTTPS: 239 alive / 14 gold
- SOCKS4: 237 alive / 152 gold
- SOCKS5: 225 alive / 143 gold

## Historical pool

- Discovered: 109324
- Ever alive: 15182
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
