# SyndProxy private pool

## Current pool

- Alive now: 1166
- Gold now: 546
- HTTP: 416 alive / 173 gold
- HTTPS: 329 alive / 79 gold
- SOCKS4: 217 alive / 147 gold
- SOCKS5: 204 alive / 147 gold

## Historical pool

- Discovered: 127333
- Ever alive: 19746
- Ever gold: 776

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
