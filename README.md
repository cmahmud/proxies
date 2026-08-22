# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 400
- HTTP: 374 alive / 84 gold
- HTTPS: 199 alive / 28 gold
- SOCKS4: 239 alive / 134 gold
- SOCKS5: 250 alive / 154 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32421
- Ever gold: 1180

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
