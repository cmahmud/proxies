# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 343
- HTTP: 336 alive / 65 gold
- HTTPS: 180 alive / 14 gold
- SOCKS4: 231 alive / 142 gold
- SOCKS5: 210 alive / 122 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15320
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
