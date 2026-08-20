# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 414
- HTTP: 263 alive / 85 gold
- HTTPS: 186 alive / 21 gold
- SOCKS4: 217 alive / 156 gold
- SOCKS5: 221 alive / 152 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27479
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
