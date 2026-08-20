# SyndProxy private pool

## Current pool

- Alive now: 668
- Gold now: 377
- HTTP: 186 alive / 58 gold
- HTTPS: 87 alive / 20 gold
- SOCKS4: 189 alive / 149 gold
- SOCKS5: 206 alive / 150 gold

## Historical pool

- Discovered: 146663
- Ever alive: 25733
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
