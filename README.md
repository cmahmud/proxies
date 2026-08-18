# SyndProxy private pool

## Current pool

- Alive now: 683
- Gold now: 254
- HTTP: 178 alive / 32 gold
- HTTPS: 92 alive / 10 gold
- SOCKS4: 223 alive / 118 gold
- SOCKS5: 190 alive / 94 gold

## Historical pool

- Discovered: 86714
- Ever alive: 6881
- Ever gold: 334

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
