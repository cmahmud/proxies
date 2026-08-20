# SyndProxy private pool

## Current pool

- Alive now: 1589
- Gold now: 630
- HTTP: 545 alive / 209 gold
- HTTPS: 485 alive / 118 gold
- SOCKS4: 229 alive / 145 gold
- SOCKS5: 330 alive / 158 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24050
- Ever gold: 968

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
