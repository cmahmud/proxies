# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 399
- HTTP: 303 alive / 101 gold
- HTTPS: 211 alive / 30 gold
- SOCKS4: 215 alive / 146 gold
- SOCKS5: 236 alive / 122 gold

## Historical pool

- Discovered: 160285
- Ever alive: 30808
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
