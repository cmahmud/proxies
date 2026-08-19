# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 542
- HTTP: 371 alive / 171 gold
- HTTPS: 229 alive / 92 gold
- SOCKS4: 210 alive / 137 gold
- SOCKS5: 221 alive / 142 gold

## Historical pool

- Discovered: 122380
- Ever alive: 18652
- Ever gold: 727

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
