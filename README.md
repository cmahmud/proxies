# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 427
- HTTP: 326 alive / 99 gold
- HTTPS: 226 alive / 26 gold
- SOCKS4: 244 alive / 152 gold
- SOCKS5: 247 alive / 150 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25189
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
