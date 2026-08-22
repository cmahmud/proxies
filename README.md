# SyndProxy private pool

## Current pool

- Alive now: 795
- Gold now: 351
- HTTP: 254 alive / 91 gold
- HTTPS: 133 alive / 26 gold
- SOCKS4: 190 alive / 111 gold
- SOCKS5: 218 alive / 123 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32577
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
