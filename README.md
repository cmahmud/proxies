# SyndProxy private pool

## Current pool

- Alive now: 881
- Gold now: 334
- HTTP: 261 alive / 64 gold
- HTTPS: 191 alive / 12 gold
- SOCKS4: 224 alive / 141 gold
- SOCKS5: 205 alive / 117 gold

## Historical pool

- Discovered: 109952
- Ever alive: 15203
- Ever gold: 490

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
