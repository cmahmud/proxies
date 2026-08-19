# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 356
- HTTP: 320 alive / 70 gold
- HTTPS: 230 alive / 12 gold
- SOCKS4: 207 alive / 129 gold
- SOCKS5: 247 alive / 145 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20361
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
