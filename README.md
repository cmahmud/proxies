# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 417
- HTTP: 259 alive / 82 gold
- HTTPS: 173 alive / 25 gold
- SOCKS4: 211 alive / 150 gold
- SOCKS5: 237 alive / 160 gold

## Historical pool

- Discovered: 154339
- Ever alive: 28898
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
