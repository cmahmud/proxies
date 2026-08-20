# SyndProxy private pool

## Current pool

- Alive now: 1593
- Gold now: 615
- HTTP: 624 alive / 215 gold
- HTTPS: 516 alive / 121 gold
- SOCKS4: 221 alive / 135 gold
- SOCKS5: 232 alive / 144 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23765
- Ever gold: 957

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
