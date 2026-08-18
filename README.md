# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 307
- HTTP: 292 alive / 36 gold
- HTTPS: 200 alive / 9 gold
- SOCKS4: 225 alive / 140 gold
- SOCKS5: 234 alive / 122 gold

## Historical pool

- Discovered: 106982
- Ever alive: 14178
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
