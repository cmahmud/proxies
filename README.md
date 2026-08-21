# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 417
- HTTP: 226 alive / 85 gold
- HTTPS: 166 alive / 25 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 245 alive / 158 gold

## Historical pool

- Discovered: 154339
- Ever alive: 28898
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
