# SyndProxy private pool

## Current pool

- Alive now: 867
- Gold now: 368
- HTTP: 293 alive / 95 gold
- HTTPS: 169 alive / 30 gold
- SOCKS4: 181 alive / 113 gold
- SOCKS5: 224 alive / 130 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32576
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
