# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 390
- HTTP: 282 alive / 85 gold
- HTTPS: 191 alive / 20 gold
- SOCKS4: 206 alive / 145 gold
- SOCKS5: 203 alive / 140 gold

## Historical pool

- Discovered: 144823
- Ever alive: 25315
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
