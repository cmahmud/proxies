# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 423
- HTTP: 303 alive / 92 gold
- HTTPS: 216 alive / 24 gold
- SOCKS4: 204 alive / 146 gold
- SOCKS5: 250 alive / 161 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28787
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
