# SyndProxy private pool

## Current pool

- Alive now: 995
- Gold now: 427
- HTTP: 319 alive / 83 gold
- HTTPS: 202 alive / 30 gold
- SOCKS4: 208 alive / 140 gold
- SOCKS5: 266 alive / 174 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32236
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
