# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 334
- HTTP: 266 alive / 64 gold
- HTTPS: 192 alive / 12 gold
- SOCKS4: 219 alive / 141 gold
- SOCKS5: 202 alive / 117 gold

## Historical pool

- Discovered: 109952
- Ever alive: 15203
- Ever gold: 490

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
