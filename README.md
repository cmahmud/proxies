# SyndProxy private pool

## Current pool

- Alive now: 861
- Gold now: 392
- HTTP: 244 alive / 88 gold
- HTTPS: 191 alive / 14 gold
- SOCKS4: 226 alive / 157 gold
- SOCKS5: 200 alive / 133 gold

## Historical pool

- Discovered: 119829
- Ever alive: 18259
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
