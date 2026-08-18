# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 339
- HTTP: 264 alive / 66 gold
- HTTPS: 200 alive / 14 gold
- SOCKS4: 226 alive / 142 gold
- SOCKS5: 209 alive / 117 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15240
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
