# SyndProxy private pool

## Current pool

- Alive now: 1187
- Gold now: 502
- HTTP: 426 alive / 173 gold
- HTTPS: 322 alive / 76 gold
- SOCKS4: 226 alive / 129 gold
- SOCKS5: 213 alive / 124 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19768
- Ever gold: 778

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
