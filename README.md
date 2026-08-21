# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 412
- HTTP: 340 alive / 100 gold
- HTTPS: 198 alive / 21 gold
- SOCKS4: 217 alive / 136 gold
- SOCKS5: 283 alive / 155 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27932
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
