# SyndProxy private pool

## Current pool

- Alive now: 784
- Gold now: 409
- HTTP: 193 alive / 85 gold
- HTTPS: 129 alive / 25 gold
- SOCKS4: 216 alive / 140 gold
- SOCKS5: 246 alive / 159 gold

## Historical pool

- Discovered: 154727
- Ever alive: 29159
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
