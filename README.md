# SyndProxy private pool

## Current pool

- Alive now: 1136
- Gold now: 557
- HTTP: 412 alive / 164 gold
- HTTPS: 276 alive / 92 gold
- SOCKS4: 232 alive / 151 gold
- SOCKS5: 216 alive / 150 gold

## Historical pool

- Discovered: 123175
- Ever alive: 18898
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
