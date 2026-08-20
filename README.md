# SyndProxy private pool

## Current pool

- Alive now: 1404
- Gold now: 606
- HTTP: 508 alive / 209 gold
- HTTPS: 407 alive / 111 gold
- SOCKS4: 233 alive / 150 gold
- SOCKS5: 256 alive / 136 gold

## Historical pool

- Discovered: 140466
- Ever alive: 23712
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
