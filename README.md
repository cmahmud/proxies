# SyndProxy private pool

## Current pool

- Alive now: 683
- Gold now: 240
- HTTP: 177 alive / 32 gold
- HTTPS: 93 alive / 8 gold
- SOCKS4: 223 alive / 111 gold
- SOCKS5: 190 alive / 89 gold

## Historical pool

- Discovered: 86714
- Ever alive: 6881
- Ever gold: 324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
