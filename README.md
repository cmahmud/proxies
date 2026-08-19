# SyndProxy private pool

## Current pool

- Alive now: 871
- Gold now: 396
- HTTP: 266 alive / 92 gold
- HTTPS: 183 alive / 14 gold
- SOCKS4: 222 alive / 157 gold
- SOCKS5: 200 alive / 133 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18246
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
