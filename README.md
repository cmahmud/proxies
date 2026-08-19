# SyndProxy private pool

## Current pool

- Alive now: 1238
- Gold now: 530
- HTTP: 453 alive / 185 gold
- HTTPS: 337 alive / 57 gold
- SOCKS4: 209 alive / 123 gold
- SOCKS5: 239 alive / 165 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19662
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
