# SyndProxy private pool

## Current pool

- Alive now: 796
- Gold now: 227
- HTTP: 284 alive / 31 gold
- HTTPS: 103 alive / 8 gold
- SOCKS4: 204 alive / 116 gold
- SOCKS5: 205 alive / 72 gold

## Historical pool

- Discovered: 92563
- Ever alive: 9315
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
