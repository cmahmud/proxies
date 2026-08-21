# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 416
- HTTP: 288 alive / 82 gold
- HTTPS: 184 alive / 23 gold
- SOCKS4: 215 alive / 150 gold
- SOCKS5: 241 alive / 161 gold

## Historical pool

- Discovered: 154339
- Ever alive: 28901
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
