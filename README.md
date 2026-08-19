# SyndProxy private pool

## Current pool

- Alive now: 850
- Gold now: 397
- HTTP: 248 alive / 93 gold
- HTTPS: 181 alive / 14 gold
- SOCKS4: 219 alive / 157 gold
- SOCKS5: 202 alive / 133 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18242
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
