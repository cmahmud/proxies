# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 384
- HTTP: 194 alive / 69 gold
- HTTPS: 127 alive / 17 gold
- SOCKS4: 219 alive / 147 gold
- SOCKS5: 220 alive / 151 gold

## Historical pool

- Discovered: 145549
- Ever alive: 25399
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
