# SyndProxy validated proxy pool

## Current pool

- Alive now: 417
- Gold now: 334
- HTTP: 79 alive / 64 gold
- HTTPS: 33 alive / 12 gold
- SOCKS4: 152 alive / 142 gold
- SOCKS5: 153 alive / 116 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48377
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
