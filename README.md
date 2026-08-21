# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 412
- HTTP: 303 alive / 90 gold
- HTTPS: 202 alive / 23 gold
- SOCKS4: 217 alive / 154 gold
- SOCKS5: 237 alive / 145 gold

## Historical pool

- Discovered: 158253
- Ever alive: 30064
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
