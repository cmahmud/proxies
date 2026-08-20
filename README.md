# SyndProxy private pool

## Current pool

- Alive now: 1483
- Gold now: 578
- HTTP: 602 alive / 202 gold
- HTTPS: 443 alive / 96 gold
- SOCKS4: 215 alive / 145 gold
- SOCKS5: 223 alive / 135 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22828
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
