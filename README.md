# SyndProxy private pool

## Current pool

- Alive now: 1230
- Gold now: 399
- HTTP: 411 alive / 91 gold
- HTTPS: 297 alive / 20 gold
- SOCKS4: 230 alive / 137 gold
- SOCKS5: 292 alive / 151 gold

## Historical pool

- Discovered: 134569
- Ever alive: 22181
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
