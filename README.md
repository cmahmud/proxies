# SyndProxy private pool

## Current pool

- Alive now: 786
- Gold now: 229
- HTTP: 269 alive / 32 gold
- HTTPS: 111 alive / 8 gold
- SOCKS4: 203 alive / 117 gold
- SOCKS5: 203 alive / 72 gold

## Historical pool

- Discovered: 92563
- Ever alive: 9323
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
