# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 367
- HTTP: 303 alive / 92 gold
- HTTPS: 165 alive / 30 gold
- SOCKS4: 189 alive / 115 gold
- SOCKS5: 230 alive / 130 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32576
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
