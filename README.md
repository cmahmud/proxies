# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 493
- HTTP: 396 alive / 137 gold
- HTTPS: 254 alive / 87 gold
- SOCKS4: 191 alive / 117 gold
- SOCKS5: 239 alive / 152 gold

## Historical pool

- Discovered: 119650
- Ever alive: 17833
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
