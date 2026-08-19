# SyndProxy private pool

## Current pool

- Alive now: 1107
- Gold now: 525
- HTTP: 405 alive / 160 gold
- HTTPS: 257 alive / 83 gold
- SOCKS4: 207 alive / 133 gold
- SOCKS5: 238 alive / 149 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18761
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
