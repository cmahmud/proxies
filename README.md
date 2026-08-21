# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 420
- HTTP: 297 alive / 93 gold
- HTTPS: 197 alive / 23 gold
- SOCKS4: 212 alive / 141 gold
- SOCKS5: 244 alive / 163 gold

## Historical pool

- Discovered: 158929
- Ever alive: 30160
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
