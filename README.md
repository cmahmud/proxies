# SyndProxy private pool

## Current pool

- Alive now: 1221
- Gold now: 370
- HTTP: 404 alive / 88 gold
- HTTPS: 253 alive / 20 gold
- SOCKS4: 244 alive / 117 gold
- SOCKS5: 320 alive / 145 gold

## Historical pool

- Discovered: 134552
- Ever alive: 22070
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
