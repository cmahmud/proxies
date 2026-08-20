# SyndProxy private pool

## Current pool

- Alive now: 711
- Gold now: 391
- HTTP: 157 alive / 82 gold
- HTTPS: 120 alive / 19 gold
- SOCKS4: 221 alive / 146 gold
- SOCKS5: 213 alive / 144 gold

## Historical pool

- Discovered: 144748
- Ever alive: 25213
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
