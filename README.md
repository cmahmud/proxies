# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 322
- HTTP: 314 alive / 58 gold
- HTTPS: 181 alive / 10 gold
- SOCKS4: 202 alive / 127 gold
- SOCKS5: 194 alive / 127 gold

## Historical pool

- Discovered: 129256
- Ever alive: 20141
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
