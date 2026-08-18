# SyndProxy private pool

## Current pool

- Alive now: 881
- Gold now: 322
- HTTP: 259 alive / 38 gold
- HTTPS: 174 alive / 9 gold
- SOCKS4: 225 alive / 142 gold
- SOCKS5: 223 alive / 133 gold

## Historical pool

- Discovered: 103711
- Ever alive: 14006
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
