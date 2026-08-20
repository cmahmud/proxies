# SyndProxy private pool

## Current pool

- Alive now: 801
- Gold now: 365
- HTTP: 210 alive / 71 gold
- HTTPS: 173 alive / 20 gold
- SOCKS4: 202 alive / 135 gold
- SOCKS5: 216 alive / 139 gold

## Historical pool

- Discovered: 149501
- Ever alive: 26712
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
