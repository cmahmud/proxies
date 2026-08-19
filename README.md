# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 357
- HTTP: 322 alive / 70 gold
- HTTPS: 234 alive / 12 gold
- SOCKS4: 204 alive / 129 gold
- SOCKS5: 255 alive / 146 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20361
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
