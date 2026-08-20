# SyndProxy private pool

## Current pool

- Alive now: 1605
- Gold now: 585
- HTTP: 628 alive / 183 gold
- HTTPS: 518 alive / 91 gold
- SOCKS4: 215 alive / 144 gold
- SOCKS5: 244 alive / 167 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24022
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
