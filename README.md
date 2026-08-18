# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 344
- HTTP: 342 alive / 65 gold
- HTTPS: 195 alive / 15 gold
- SOCKS4: 239 alive / 141 gold
- SOCKS5: 213 alive / 123 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15315
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
