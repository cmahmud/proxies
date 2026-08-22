# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 408
- HTTP: 214 alive / 85 gold
- HTTPS: 172 alive / 27 gold
- SOCKS4: 200 alive / 138 gold
- SOCKS5: 247 alive / 158 gold

## Historical pool

- Discovered: 162241
- Ever alive: 31414
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
