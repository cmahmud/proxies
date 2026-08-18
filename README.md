# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 251
- HTTP: 334 alive / 35 gold
- HTTPS: 195 alive / 7 gold
- SOCKS4: 221 alive / 144 gold
- SOCKS5: 158 alive / 65 gold

## Historical pool

- Discovered: 102872
- Ever alive: 13695
- Ever gold: 428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
