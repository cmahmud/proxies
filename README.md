# SyndProxy private pool

## Current pool

- Alive now: 1087
- Gold now: 527
- HTTP: 384 alive / 150 gold
- HTTPS: 282 alive / 108 gold
- SOCKS4: 222 alive / 144 gold
- SOCKS5: 199 alive / 125 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19946
- Ever gold: 806

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
