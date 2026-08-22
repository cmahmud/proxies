# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 363
- HTTP: 304 alive / 92 gold
- HTTPS: 163 alive / 30 gold
- SOCKS4: 193 alive / 112 gold
- SOCKS5: 231 alive / 129 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32576
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
