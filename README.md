# SyndProxy private pool

## Current pool

- Alive now: 1177
- Gold now: 509
- HTTP: 422 alive / 173 gold
- HTTPS: 325 alive / 83 gold
- SOCKS4: 219 alive / 128 gold
- SOCKS5: 211 alive / 125 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19767
- Ever gold: 778

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
