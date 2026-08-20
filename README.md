# SyndProxy private pool

## Current pool

- Alive now: 1566
- Gold now: 591
- HTTP: 547 alive / 196 gold
- HTTPS: 468 alive / 93 gold
- SOCKS4: 234 alive / 145 gold
- SOCKS5: 317 alive / 157 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24050
- Ever gold: 968

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
