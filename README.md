# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 380
- HTTP: 325 alive / 85 gold
- HTTPS: 215 alive / 26 gold
- SOCKS4: 216 alive / 124 gold
- SOCKS5: 226 alive / 145 gold

## Historical pool

- Discovered: 164181
- Ever alive: 32044
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
