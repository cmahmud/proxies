# SyndProxy private pool

## Current pool

- Alive now: 1575
- Gold now: 585
- HTTP: 648 alive / 198 gold
- HTTPS: 425 alive / 96 gold
- SOCKS4: 232 alive / 140 gold
- SOCKS5: 270 alive / 151 gold

## Historical pool

- Discovered: 136252
- Ever alive: 22759
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
