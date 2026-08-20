# SyndProxy private pool

## Current pool

- Alive now: 861
- Gold now: 391
- HTTP: 250 alive / 86 gold
- HTTPS: 209 alive / 20 gold
- SOCKS4: 203 alive / 145 gold
- SOCKS5: 199 alive / 140 gold

## Historical pool

- Discovered: 144823
- Ever alive: 25321
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
