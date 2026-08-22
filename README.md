# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 399
- HTTP: 303 alive / 93 gold
- HTTPS: 192 alive / 25 gold
- SOCKS4: 225 alive / 145 gold
- SOCKS5: 211 alive / 136 gold

## Historical pool

- Discovered: 165824
- Ever alive: 32344
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
