# SyndProxy private pool

## Current pool

- Alive now: 889
- Gold now: 407
- HTTP: 225 alive / 88 gold
- HTTPS: 190 alive / 24 gold
- SOCKS4: 210 alive / 127 gold
- SOCKS5: 264 alive / 168 gold

## Historical pool

- Discovered: 164909
- Ever alive: 32128
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
