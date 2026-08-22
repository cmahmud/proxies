# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 424
- HTTP: 361 alive / 87 gold
- HTTPS: 199 alive / 29 gold
- SOCKS4: 205 alive / 140 gold
- SOCKS5: 242 alive / 168 gold

## Historical pool

- Discovered: 163875
- Ever alive: 32029
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
