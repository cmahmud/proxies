# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 390
- HTTP: 288 alive / 79 gold
- HTTPS: 165 alive / 20 gold
- SOCKS4: 231 alive / 148 gold
- SOCKS5: 237 alive / 143 gold

## Historical pool

- Discovered: 156831
- Ever alive: 29631
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
