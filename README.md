# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 365
- HTTP: 365 alive / 73 gold
- HTTPS: 260 alive / 11 gold
- SOCKS4: 205 alive / 127 gold
- SOCKS5: 234 alive / 154 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20377
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
