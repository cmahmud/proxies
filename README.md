# SyndProxy private pool

## Current pool

- Alive now: 1240
- Gold now: 414
- HTTP: 486 alive / 99 gold
- HTTPS: 291 alive / 27 gold
- SOCKS4: 220 alive / 141 gold
- SOCKS5: 243 alive / 147 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31733
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
