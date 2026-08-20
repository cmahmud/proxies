# SyndProxy private pool

## Current pool

- Alive now: 1836
- Gold now: 647
- HTTP: 710 alive / 221 gold
- HTTPS: 608 alive / 116 gold
- SOCKS4: 219 alive / 148 gold
- SOCKS5: 299 alive / 162 gold

## Historical pool

- Discovered: 142688
- Ever alive: 24273
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
