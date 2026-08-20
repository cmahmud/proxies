# SyndProxy private pool

## Current pool

- Alive now: 1504
- Gold now: 623
- HTTP: 574 alive / 207 gold
- HTTPS: 460 alive / 114 gold
- SOCKS4: 232 alive / 144 gold
- SOCKS5: 238 alive / 158 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24031
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
