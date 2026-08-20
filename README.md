# SyndProxy private pool

## Current pool

- Alive now: 1251
- Gold now: 574
- HTTP: 497 alive / 196 gold
- HTTPS: 302 alive / 95 gold
- SOCKS4: 232 alive / 148 gold
- SOCKS5: 220 alive / 135 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22850
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
