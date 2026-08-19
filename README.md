# SyndProxy private pool

## Current pool

- Alive now: 1190
- Gold now: 545
- HTTP: 419 alive / 183 gold
- HTTPS: 322 alive / 68 gold
- SOCKS4: 234 alive / 148 gold
- SOCKS5: 215 alive / 146 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19768
- Ever gold: 786

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
