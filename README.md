# SyndProxy private pool

## Current pool

- Alive now: 693
- Gold now: 239
- HTTP: 178 alive / 31 gold
- HTTPS: 101 alive / 8 gold
- SOCKS4: 223 alive / 111 gold
- SOCKS5: 191 alive / 89 gold

## Historical pool

- Discovered: 86714
- Ever alive: 6881
- Ever gold: 323

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
