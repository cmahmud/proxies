# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 349
- HTTP: 278 alive / 62 gold
- HTTPS: 247 alive / 19 gold
- SOCKS4: 226 alive / 146 gold
- SOCKS5: 210 alive / 122 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15387
- Ever gold: 496

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
