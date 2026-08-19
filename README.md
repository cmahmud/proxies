# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 497
- HTTP: 278 alive / 122 gold
- HTTPS: 191 alive / 70 gold
- SOCKS4: 214 alive / 150 gold
- SOCKS5: 227 alive / 155 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16784
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
