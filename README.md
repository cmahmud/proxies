# SyndProxy private pool

## Current pool

- Alive now: 1542
- Gold now: 644
- HTTP: 587 alive / 216 gold
- HTTPS: 487 alive / 106 gold
- SOCKS4: 220 alive / 152 gold
- SOCKS5: 248 alive / 170 gold

## Historical pool

- Discovered: 141226
- Ever alive: 23976
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
