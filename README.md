# SyndProxy private pool

## Current pool

- Alive now: 886
- Gold now: 368
- HTTP: 240 alive / 82 gold
- HTTPS: 212 alive / 21 gold
- SOCKS4: 211 alive / 124 gold
- SOCKS5: 223 alive / 141 gold

## Historical pool

- Discovered: 164909
- Ever alive: 32120
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
