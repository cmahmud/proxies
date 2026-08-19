# SyndProxy private pool

## Current pool

- Alive now: 1147
- Gold now: 546
- HTTP: 416 alive / 189 gold
- HTTPS: 300 alive / 79 gold
- SOCKS4: 227 alive / 133 gold
- SOCKS5: 204 alive / 145 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19817
- Ever gold: 798

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
