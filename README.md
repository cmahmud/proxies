# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 402
- HTTP: 328 alive / 86 gold
- HTTPS: 232 alive / 25 gold
- SOCKS4: 209 alive / 145 gold
- SOCKS5: 254 alive / 146 gold

## Historical pool

- Discovered: 165842
- Ever alive: 32372
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
