# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 385
- HTTP: 100 alive / 58 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 171 alive / 152 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33433
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
