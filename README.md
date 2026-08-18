# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 240
- HTTP: 402 alive / 32 gold
- HTTPS: 145 alive / 7 gold
- SOCKS4: 202 alive / 110 gold
- SOCKS5: 198 alive / 91 gold

## Historical pool

- Discovered: 91718
- Ever alive: 9022
- Ever gold: 360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
