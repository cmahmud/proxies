# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 459
- HTTP: 133 alive / 88 gold
- HTTPS: 136 alive / 36 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46856
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
