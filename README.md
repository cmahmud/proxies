# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 413
- HTTP: 392 alive / 112 gold
- HTTPS: 258 alive / 28 gold
- SOCKS4: 230 alive / 151 gold
- SOCKS5: 216 alive / 122 gold

## Historical pool

- Discovered: 160024
- Ever alive: 30569
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
