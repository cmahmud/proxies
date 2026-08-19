# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 490
- HTTP: 389 alive / 130 gold
- HTTPS: 250 alive / 86 gold
- SOCKS4: 200 alive / 122 gold
- SOCKS5: 236 alive / 152 gold

## Historical pool

- Discovered: 119650
- Ever alive: 17840
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
