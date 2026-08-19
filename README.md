# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 521
- HTTP: 352 alive / 160 gold
- HTTPS: 283 alive / 90 gold
- SOCKS4: 203 alive / 141 gold
- SOCKS5: 204 alive / 130 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18428
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
