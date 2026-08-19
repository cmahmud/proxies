# SyndProxy private pool

## Current pool

- Alive now: 1150
- Gold now: 412
- HTTP: 373 alive / 81 gold
- HTTPS: 243 alive / 15 gold
- SOCKS4: 259 alive / 155 gold
- SOCKS5: 275 alive / 161 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20702
- Ever gold: 874

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
