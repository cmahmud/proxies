# SyndProxy private pool

## Current pool

- Alive now: 1130
- Gold now: 424
- HTTP: 385 alive / 100 gold
- HTTPS: 311 alive / 31 gold
- SOCKS4: 192 alive / 132 gold
- SOCKS5: 242 alive / 161 gold

## Historical pool

- Discovered: 161019
- Ever alive: 31116
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
