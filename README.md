# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 387
- HTTP: 316 alive / 82 gold
- HTTPS: 177 alive / 15 gold
- SOCKS4: 221 alive / 157 gold
- SOCKS5: 204 alive / 133 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18228
- Ever gold: 717

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
