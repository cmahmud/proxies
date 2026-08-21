# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 420
- HTTP: 222 alive / 86 gold
- HTTPS: 161 alive / 26 gold
- SOCKS4: 209 alive / 149 gold
- SOCKS5: 252 alive / 159 gold

## Historical pool

- Discovered: 154339
- Ever alive: 28893
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
