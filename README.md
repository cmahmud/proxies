# SyndProxy private pool

## Current pool

- Alive now: 877
- Gold now: 356
- HTTP: 306 alive / 92 gold
- HTTPS: 167 alive / 28 gold
- SOCKS4: 188 alive / 111 gold
- SOCKS5: 216 alive / 125 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32576
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
