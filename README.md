# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 525
- HTTP: 377 alive / 170 gold
- HTTPS: 239 alive / 92 gold
- SOCKS4: 206 alive / 129 gold
- SOCKS5: 216 alive / 134 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18777
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
