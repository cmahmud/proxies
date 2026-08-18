# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 249
- HTTP: 327 alive / 34 gold
- HTTPS: 171 alive / 8 gold
- SOCKS4: 225 alive / 141 gold
- SOCKS5: 164 alive / 66 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13714
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
