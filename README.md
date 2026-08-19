# SyndProxy private pool

## Current pool

- Alive now: 1195
- Gold now: 502
- HTTP: 407 alive / 146 gold
- HTTPS: 337 alive / 93 gold
- SOCKS4: 204 alive / 123 gold
- SOCKS5: 247 alive / 140 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17339
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
