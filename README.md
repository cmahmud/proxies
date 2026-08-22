# SyndProxy private pool

## Current pool

- Alive now: 808
- Gold now: 382
- HTTP: 219 alive / 87 gold
- HTTPS: 172 alive / 29 gold
- SOCKS4: 209 alive / 138 gold
- SOCKS5: 208 alive / 128 gold

## Historical pool

- Discovered: 162765
- Ever alive: 31630
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
