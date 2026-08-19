# SyndProxy private pool

## Current pool

- Alive now: 1213
- Gold now: 538
- HTTP: 437 alive / 182 gold
- HTTPS: 320 alive / 61 gold
- SOCKS4: 237 alive / 148 gold
- SOCKS5: 219 alive / 147 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19771
- Ever gold: 786

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
