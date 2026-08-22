# SyndProxy private pool

## Current pool

- Alive now: 900
- Gold now: 399
- HTTP: 278 alive / 93 gold
- HTTPS: 186 alive / 25 gold
- SOCKS4: 223 alive / 147 gold
- SOCKS5: 213 alive / 134 gold

## Historical pool

- Discovered: 165825
- Ever alive: 32346
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
