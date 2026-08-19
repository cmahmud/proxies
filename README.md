# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 527
- HTTP: 333 alive / 154 gold
- HTTPS: 251 alive / 91 gold
- SOCKS4: 211 alive / 147 gold
- SOCKS5: 211 alive / 135 gold

## Historical pool

- Discovered: 127371
- Ever alive: 19897
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
