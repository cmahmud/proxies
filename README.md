# SyndProxy private pool

## Current pool

- Alive now: 795
- Gold now: 408
- HTTP: 216 alive / 96 gold
- HTTPS: 144 alive / 24 gold
- SOCKS4: 205 alive / 136 gold
- SOCKS5: 230 alive / 152 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29176
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
