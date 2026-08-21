# SyndProxy private pool

## Current pool

- Alive now: 901
- Gold now: 423
- HTTP: 264 alive / 95 gold
- HTTPS: 185 alive / 23 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 239 alive / 164 gold

## Historical pool

- Discovered: 158929
- Ever alive: 30164
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
