# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 386
- HTTP: 290 alive / 82 gold
- HTTPS: 206 alive / 25 gold
- SOCKS4: 200 alive / 124 gold
- SOCKS5: 258 alive / 155 gold

## Historical pool

- Discovered: 164912
- Ever alive: 32137
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
